import sys, os, re, cv2, stat
from PyQt5.QtWidgets import QWidget,QDialog,QApplication,QFileDialog

import images_to_size_UI



class MyWindow(QDialog, QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = images_to_size_UI.Ui_Resizer()
        self.ui.setupUi(self)
        
        self.log = ''
        self.additional_resolutions = []
        # go on setting up your handlers like:
        # self.ui.okButton.clicked.connect(function_name)
        # etc...
    
        self.ui.toolButton_Path.clicked.connect(lambda: self.set_directory())
        self.ui.pushButton_Run.clicked.connect(lambda: self.Run())
        self.ui.pushButton_add_additional_resolution.clicked.connect(lambda: self.add_resolution())
        self.ui.pushButton_delete_additional_resolution.clicked.connect(lambda: self.del_resolution())

    
    def keyPressEvent(self, e):
        if e.key() == 16777220:
            print('OK')
        
        
        
    def add_log(self, info, color):
        self.log += info + '\n'
        self.ui.label_log_text.setText(self.log)
        self.ui.label_log_text.setStyleSheet('color: {}'.format(color))

    def set_directory(self):
        self.ui.lineEdit_Path.setText(QFileDialog.getExistingDirectory())


    def add_resolution(self):
        log    = ''
        self.ui.label_log_text_add.setText(log)

        x      = int(self.ui.lineEdit_add_X.text())
        y      = int(self.ui.lineEdit_add_Y.text())
        prefix = self.ui.lineEdit_add_prefix.text()
        file_format = self.ui.comboBox_add_file_format.currentText()

        self.additional_resolutions.append([prefix, x, y, file_format])

        for n, info in enumerate(self.additional_resolutions):
            log += '{}.  prefix: "{}",  resolution: {}x{},  file format: {}'.format(n+1,*info)  + '\n'

        self.ui.label_log_text_add.setText(log)
        self.ui.label_log_text_add.setStyleSheet('color: green')


    def del_resolution(self):
        log    = ''
        self.ui.label_log_text_add.setText(log)
        
        if len(self.additional_resolutions) > 0:
            self.additional_resolutions.pop()

            for n, info in enumerate(self.additional_resolutions):
                log += '{}.  prefix: "{}",  resolution: {}x{},  file format: {}'.format(n+1,*info)  + '\n'

        self.ui.label_log_text_add.setText(log)
        self.ui.label_log_text_add.setStyleSheet('color: green')


    def save_additional_resolutions(self, image, image_path, additional_resolutions):

        for prefix, x, y, file_format in self.additional_resolutions:
            path, file = os.path.split(image_path)
            name = file.split('.')[0]

            fullpath = path +'/'+ name + prefix + file_format
            _image = cv2.resize(image.copy(), (x, y))
            cv2.imwrite(fullpath, _image)

            info = "{}".format(fullpath)
            self.add_log(info, color='green')    
        
        
    def Run(self):
        self.log = ""

        x = int(self.ui.lineEdit_resize_to_X.text())
        y = int(self.ui.lineEdit_resize_to_Y.text())
        resolution= (x,y)

        threshold_X = int(self.ui.lineEdit_image_size_X.text())
        threshold_Y = int(self.ui.lineEdit_image_size_Y.text())

        self.ui.progressBar.setValue(0)

        # GET DIR PATHS
        paths  = []
        for i in os.walk(self.ui.lineEdit_Path.text()):
            if os.path.isdir(i[0]):
                paths.append(i[0])

        #GET IMAGES FULL PATH 
        images = []        
        for path in paths:        
            for file in os.listdir(path):
                fullpath = path+'/'+file

                pattern = '.*(\{pattern})$'.format(pattern=self.ui.comboBox_findall_from.currentText())                                      
                findall = re.findall(pattern ,file)

                if self.ui.comboBox_findall_from.currentText() in findall:
                    if self.ui.lineEdit_findall.text() in file:
                        images.append(fullpath)


        if images:
            #PROGRESS BAR
            progressBar_value = int(100/len(images))
            progress = 0

            # RESIZE        
            for image_path in images:
                os.chmod(image_path, stat.S_IWRITE)
                original_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

                if original_image.shape[1] > threshold_X and original_image.shape[0] > threshold_Y:
                    image = cv2.resize(original_image.copy(), resolution)
                    
                    if bool(self.ui.checkBox_Delete_Alpha_Chanel.checkState()):
                        if len(image.shape) > 2:
                            cv2.imwrite(image_path, image[:,:,:3])
                            self.save_additional_resolutions(original_image[:,:,:3], image_path, self.additional_resolutions)

                        else:
                            self.save_additional_resolutions(original_image, image_path, self.additional_resolutions)
                            cv2.imwrite(image_path, image)
                    else:
                        self.save_additional_resolutions(original_image, image_path, self.additional_resolutions)
                        cv2.imwrite(image_path, image)


                    info = "{}".format(image_path)
                    self.add_log(info, color='green')

                #PROGRESS BAR
                progress = progress + progressBar_value
                self.ui.progressBar.setValue(progress)
            #PROGRESS BAR    
            self.ui.progressBar.setValue(100)

        else:
            info = "There are no images in the current directory!"
            self.add_log(info, color ='red')
        
        
        

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
        
    w = MyWindow()
    w.show()
    app.exec_()