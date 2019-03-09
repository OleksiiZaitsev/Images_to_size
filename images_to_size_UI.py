# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'images_to_size.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Resizer(object):
    def setupUi(self, Resizer):
        Resizer.setObjectName("Resizer")
        Resizer.resize(520, 494)
        Resizer.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"\n"
"   background-color: #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Resizer)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(Resizer)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 9, 7, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 55))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_log_text = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_log_text.sizePolicy().hasHeightForWidth())
        self.label_log_text.setSizePolicy(sizePolicy)
        self.label_log_text.setText("")
        self.label_log_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_log_text.setWordWrap(True)
        self.label_log_text.setOpenExternalLinks(False)
        self.label_log_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_log_text.setObjectName("label_log_text")
        self.verticalLayout.addWidget(self.label_log_text)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 17, 0, 1, 9)
        self.comboBox_add_file_format = QtWidgets.QComboBox(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_add_file_format.sizePolicy().hasHeightForWidth())
        self.comboBox_add_file_format.setSizePolicy(sizePolicy)
        self.comboBox_add_file_format.setObjectName("comboBox_add_file_format")
        self.comboBox_add_file_format.addItem("")
        self.comboBox_add_file_format.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_add_file_format, 12, 7, 1, 2)
        self.lineEdit_image_size_X = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_image_size_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_image_size_X.setSizePolicy(sizePolicy)
        self.lineEdit_image_size_X.setObjectName("lineEdit_image_size_X")
        self.gridLayout_2.addWidget(self.lineEdit_image_size_X, 4, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 5, 1, 1)
        self.pushButton_delete_additional_resolution = QtWidgets.QPushButton(Resizer)
        self.pushButton_delete_additional_resolution.setObjectName("pushButton_delete_additional_resolution")
        self.gridLayout_2.addWidget(self.pushButton_delete_additional_resolution, 11, 7, 1, 2)
        self.lineEdit_add_Y = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_add_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_Y.setSizePolicy(sizePolicy)
        self.lineEdit_add_Y.setObjectName("lineEdit_add_Y")
        self.gridLayout_2.addWidget(self.lineEdit_add_Y, 12, 6, 1, 1)
        self.label_29 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 12, 5, 1, 1)
        self.lineEdit_add_prefix = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_add_prefix.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_prefix.setSizePolicy(sizePolicy)
        self.lineEdit_add_prefix.setObjectName("lineEdit_add_prefix")
        self.gridLayout_2.addWidget(self.lineEdit_add_prefix, 12, 1, 1, 1)
        self.lineEdit_add_X = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_add_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_X.setSizePolicy(sizePolicy)
        self.lineEdit_add_X.setObjectName("lineEdit_add_X")
        self.gridLayout_2.addWidget(self.lineEdit_add_X, 12, 4, 1, 1)
        self.pushButton_add_additional_resolution = QtWidgets.QPushButton(Resizer)
        self.pushButton_add_additional_resolution.setObjectName("pushButton_add_additional_resolution")
        self.gridLayout_2.addWidget(self.pushButton_add_additional_resolution, 11, 6, 1, 1)
        self.lineEdit_findall = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_findall.sizePolicy().hasHeightForWidth())
        self.lineEdit_findall.setSizePolicy(sizePolicy)
        self.lineEdit_findall.setText("")
        self.lineEdit_findall.setObjectName("lineEdit_findall")
        self.gridLayout_2.addWidget(self.lineEdit_findall, 9, 4, 1, 3)
        self.label_28 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 12, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 9, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(Resizer)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 6, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 3, 1, 1)
        self.lineEdit_image_size_Y = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_image_size_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_image_size_Y.setSizePolicy(sizePolicy)
        self.lineEdit_image_size_Y.setObjectName("lineEdit_image_size_Y")
        self.gridLayout_2.addWidget(self.lineEdit_image_size_Y, 4, 6, 1, 1)
        self.comboBox_findall_from = QtWidgets.QComboBox(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_findall_from.sizePolicy().hasHeightForWidth())
        self.comboBox_findall_from.setSizePolicy(sizePolicy)
        self.comboBox_findall_from.setObjectName("comboBox_findall_from")
        self.comboBox_findall_from.addItem("")
        self.comboBox_findall_from.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_findall_from, 4, 7, 1, 2)
        self.label_3 = QtWidgets.QLabel(Resizer)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: orange")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 9)
        self.label_10 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 3, 1, 1)
        self.toolButton_Path = QtWidgets.QToolButton(Resizer)
        self.toolButton_Path.setObjectName("toolButton_Path")
        self.gridLayout_2.addWidget(self.toolButton_Path, 8, 8, 1, 1)
        self.comboBox_findall_to = QtWidgets.QComboBox(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_findall_to.sizePolicy().hasHeightForWidth())
        self.comboBox_findall_to.setSizePolicy(sizePolicy)
        self.comboBox_findall_to.setObjectName("comboBox_findall_to")
        self.comboBox_findall_to.addItem("")
        self.comboBox_findall_to.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_findall_to, 5, 7, 1, 2)
        self.label_6 = QtWidgets.QLabel(Resizer)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 8, 7, 1, 1)
        self.lineEdit_resize_to_X = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_resize_to_X.sizePolicy().hasHeightForWidth())
        self.lineEdit_resize_to_X.setSizePolicy(sizePolicy)
        self.lineEdit_resize_to_X.setObjectName("lineEdit_resize_to_X")
        self.gridLayout_2.addWidget(self.lineEdit_resize_to_X, 5, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(Resizer)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 9, 0, 1, 2)
        self.label_27 = QtWidgets.QLabel(Resizer)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 11, 0, 1, 6)
        self.line_10 = QtWidgets.QFrame(Resizer)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 10, 0, 1, 9)
        self.label_2 = QtWidgets.QLabel(Resizer)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 2)
        self.label_30 = QtWidgets.QLabel(Resizer)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 12, 0, 1, 1)
        self.lineEdit_resize_to_Y = QtWidgets.QLineEdit(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_resize_to_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_resize_to_Y.setSizePolicy(sizePolicy)
        self.lineEdit_resize_to_Y.setObjectName("lineEdit_resize_to_Y")
        self.gridLayout_2.addWidget(self.lineEdit_resize_to_Y, 5, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(Resizer)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 7, 0, 1, 9)
        self.label_5 = QtWidgets.QLabel(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 2, 1, 1)
        self.lineEdit_Path = QtWidgets.QLineEdit(Resizer)
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.gridLayout_2.addWidget(self.lineEdit_Path, 8, 0, 1, 7)
        self.label = QtWidgets.QLabel(Resizer)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 2)
        self.checkBox_Delete_Alpha_Chanel = QtWidgets.QCheckBox(Resizer)
        self.checkBox_Delete_Alpha_Chanel.setChecked(False)
        self.checkBox_Delete_Alpha_Chanel.setObjectName("checkBox_Delete_Alpha_Chanel")
        self.gridLayout_2.addWidget(self.checkBox_Delete_Alpha_Chanel, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(Resizer)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 9)
        self.line_4 = QtWidgets.QFrame(Resizer)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 3, 0, 1, 9)
        self.progressBar = QtWidgets.QProgressBar(Resizer)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 16, 0, 1, 9)
        self.line_3 = QtWidgets.QFrame(Resizer)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 14, 0, 1, 9)
        self.scrollArea_add = QtWidgets.QScrollArea(Resizer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_add.sizePolicy().hasHeightForWidth())
        self.scrollArea_add.setSizePolicy(sizePolicy)
        self.scrollArea_add.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_add.setWidgetResizable(True)
        self.scrollArea_add.setObjectName("scrollArea_add")
        self.scrollAreaWidgetContents_add = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_add.setGeometry(QtCore.QRect(0, 0, 491, 54))
        self.scrollAreaWidgetContents_add.setObjectName("scrollAreaWidgetContents_add")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_add)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_add = QtWidgets.QVBoxLayout()
        self.verticalLayout_add.setObjectName("verticalLayout_add")
        self.label_log_text_add = QtWidgets.QLabel(self.scrollAreaWidgetContents_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_log_text_add.sizePolicy().hasHeightForWidth())
        self.label_log_text_add.setSizePolicy(sizePolicy)
        self.label_log_text_add.setText("")
        self.label_log_text_add.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_log_text_add.setWordWrap(True)
        self.label_log_text_add.setOpenExternalLinks(False)
        self.label_log_text_add.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_log_text_add.setObjectName("label_log_text_add")
        self.verticalLayout_add.addWidget(self.label_log_text_add)
        self.horizontalLayout_5.addLayout(self.verticalLayout_add)
        self.scrollArea_add.setWidget(self.scrollAreaWidgetContents_add)
        self.gridLayout_2.addWidget(self.scrollArea_add, 13, 0, 1, 9)
        self.pushButton_Run = QtWidgets.QPushButton(Resizer)
        self.pushButton_Run.setStyleSheet("")
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.gridLayout_2.addWidget(self.pushButton_Run, 15, 0, 1, 9)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Resizer)
        QtCore.QMetaObject.connectSlotsByName(Resizer)

    def retranslateUi(self, Resizer):
        _translate = QtCore.QCoreApplication.translate
        Resizer.setWindowTitle(_translate("Resizer", "Resizer"))
        self.label_13.setText(_translate("Resizer", "(if nessesary)"))
        self.comboBox_add_file_format.setItemText(0, _translate("Resizer", ".png"))
        self.comboBox_add_file_format.setItemText(1, _translate("Resizer", ".jpg"))
        self.lineEdit_image_size_X.setText(_translate("Resizer", "512"))
        self.label_9.setText(_translate("Resizer", "y"))
        self.pushButton_delete_additional_resolution.setText(_translate("Resizer", "delete"))
        self.lineEdit_add_Y.setText(_translate("Resizer", "256"))
        self.label_29.setText(_translate("Resizer", "y"))
        self.lineEdit_add_prefix.setText(_translate("Resizer", "_256"))
        self.lineEdit_add_X.setText(_translate("Resizer", "256"))
        self.pushButton_add_additional_resolution.setText(_translate("Resizer", "add"))
        self.label_28.setText(_translate("Resizer", "x"))
        self.label_12.setText(_translate("Resizer", ":"))
        self.label_7.setText(_translate("Resizer", "x"))
        self.lineEdit_image_size_Y.setText(_translate("Resizer", "512"))
        self.comboBox_findall_from.setItemText(0, _translate("Resizer", ".png"))
        self.comboBox_findall_from.setItemText(1, _translate("Resizer", ".jpg"))
        self.label_3.setText(_translate("Resizer", "Will change resolution for all images in setted directory, be careful!"))
        self.label_10.setText(_translate("Resizer", "y"))
        self.label_8.setText(_translate("Resizer", "x"))
        self.toolButton_Path.setText(_translate("Resizer", "..."))
        self.comboBox_findall_to.setItemText(0, _translate("Resizer", ".png"))
        self.comboBox_findall_to.setItemText(1, _translate("Resizer", ".jpg"))
        self.label_6.setText(_translate("Resizer", "directory"))
        self.lineEdit_resize_to_X.setText(_translate("Resizer", "512"))
        self.label_4.setText(_translate("Resizer", ":"))
        self.label_11.setText(_translate("Resizer", "image name filter by pattern"))
        self.label_27.setText(_translate("Resizer", "Press add if you need to generate other additional resolutions!"))
        self.label_2.setText(_translate("Resizer", "resize to"))
        self.label_30.setText(_translate("Resizer", "postfix"))
        self.lineEdit_resize_to_Y.setText(_translate("Resizer", "512"))
        self.label_5.setText(_translate("Resizer", ":"))
        self.label.setText(_translate("Resizer", "if image resolution more than "))
        self.checkBox_Delete_Alpha_Chanel.setText(_translate("Resizer", "Delete Alpha Chanel"))
        self.pushButton_Run.setText(_translate("Resizer", "Run!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Resizer = QtWidgets.QDialog()
    ui = Ui_Resizer()
    ui.setupUi(Resizer)
    Resizer.show()
    sys.exit(app.exec_())

