from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from selenium import*
from selenium import webdriver
import os
from time import sleep
import datetime as dt
from datetime import datetime


class Ui_MainWindow(object):
    
    def windowsec(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Window2()
        self.ui.setupUi(self.window)
        self.window.show()

    global chatv
    global joinv
    global videov
    global audiov
    global speedv
    def sleep(self):
        self.s=self.spinBox.value()
        if (self.s==1):
            self.label_process.setText("internet must have 1 mb /s  ")
            self.speedv = 2
        if (self.s==2):
            self.label_process.setText("internet must have normal speed ")
            self.speedv = 3    
        if (self.s==3):
            self.label_process.setText("internet may be slow ")
            self.speedv = 5

    def chat(self):
        self.a =self.checkBox_chat.checkState()
        if (self.a==2):
            self.label_process.setText("Chat is Enabled")
            self.chatv = 1
        else :
            self.label_process.setText("Chat is disabled")
            self.chatv = 0

    def join(self):
        self.d =self.checkBox_join.checkState()
        if (self.d==2):
            self.label_process.setText("join is Enabled")
            self.joinv = 1
        else :
            self.label_process.setText("join is disabled")
            self.joinv = 0
        
    def video(self):
        self.b =self.checkBox_video.checkState()
        if (self.b==2):
            self.label_process.setText("video is Enabled")
            self.videov = 1
        else :
            self.label_process.setText("video is disabled")
            self.videov = 0

    def audio(self):
        self.c =self.checkBox_audio.checkState()
        if (self.c==2):
            self.label_process.setText("audio is Enabled")
            self.audiov = 1
        else :
            self.label_process.setText("audio is disabled")
            self.audiov = 0

    def start_main(self):
        print("hi")

        while (True):
            n=self.timeEdit_timing.time() #geting window timnig
            add_timing=(n.addSecs(50).toString(Qt.ISODate)) ## add of timinig to lable

            current_timing=QTime.currentTime() ###current timig
            timig_org=(current_timing.toString()) ### cuting milisecond
            print (timig_org)
            print(add_timing)

            # print (dt.datetime.now().hour)
            # print  (dt.datetime.now().minute)

            # current_hour = dt.datetime.now().hour
            # current_min = dt.datetime.now().minute
            if (timig_org==add_timing):
                print("hi")
                self.url=self.lineEdit_id.text()
                #self.a =("https://meet.google.com/"+str(self.url))
                self.a="https://meet.google.com/wbn-zbnx-csc"
                print (self.chatv)
                print (self.videov)
                print (self.audiov)

                print (self.joinv)
                print (self.speedv)

                self.browser = webdriver.Firefox("C:\\Users\\sk\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\i39cxzmn.sk")
                self.browser.get(self.a)
                sleep(self.speedv)
                if (self.audiov==0):
                    self.browser.find_element_by_class_name ("DPvwYc").click()

                if (self.videov==0):
                    self.browser.find_element_by_class_name("I5fjHe").click()
                    

                if (self.joinv==1):
                    sleep(self.speedv)
                    self.browser.find_element_by_class_name("NPEfkd").click()
                    # sleep(3600)
                    # self.browser.find_element_by_css_selector(".GaONte").click()
                    
                if (self.chatv==1):
                    sleep(6)
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys("Good Morning To All")
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span").click()
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button").click()
                    
                if (self.chatv==1):
                    sleep(3)
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys("Thank You")
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span").click()
                    self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button").click()
                
                if (self.joinv==1):
                    sleep(10)
                    self.browser.find_element_by_css_selector(".GaONte").click()
                    exit(0)
    def setupUi(self, MainWindow):
        self.chatv =0
        self.joinv=0
        self.videov=0
        self.audiov=0
        self.speedv=2
        ############ assing value #################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 341)
        MainWindow.setStyleSheet("background-color: rgb(48, 200, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(30, 20, 421, 41))
        self.label_info.setStyleSheet("font: 14pt \"Segoe MDL2 Assets\";\n""background-color: rgb(229, 229, 68);")
        self.label_info.setObjectName("label_info")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(140, 100, 181, 31))
        self.lineEdit_id.setDragEnabled(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.timeEdit_timing = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_timing.setGeometry(QtCore.QRect(140, 160, 181, 31))
        self.timeEdit_timing.setAccelerated(True)
        self.timeEdit_timing.setCalendarPopup(False)
        self.timeEdit_timing.setObjectName("timeEdit_timing")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(40, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_set_timing = QtWidgets.QLabel(self.centralwidget)
        self.label_set_timing.setGeometry(QtCore.QRect(40, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_set_timing.setFont(font)
        self.label_set_timing.setObjectName("label_set_timing")

        self.checkBox_join = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_join.setGeometry(QtCore.QRect(420, 100, 41, 21))
        self.checkBox_join.setChecked(False)
        self.checkBox_join.setObjectName("checkBox_join")

        self.checkBox_audio = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_audio.setGeometry(QtCore.QRect(350, 100, 51, 21))
        self.checkBox_audio.setChecked(False)
        self.checkBox_audio.setObjectName("checkBox_audio")

        self.checkBox_video = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_video.setGeometry(QtCore.QRect(350, 170, 51, 17))
        self.checkBox_video.setObjectName("checkBox_video")

        self.checkBox_chat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chat.setGeometry(QtCore.QRect(420, 170, 41, 20))
        self.checkBox_chat.setObjectName("checkBox_chat")
        self.label_process = QtWidgets.QLabel(self.centralwidget)
        self.label_process.setGeometry(QtCore.QRect(140, 230, 201, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 211, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_process.setPalette(palette)
        self.label_process.setAutoFillBackground(False)
        self.label_process.setStyleSheet("background-color: rgb(236, 211, 18);\n""font: 9pt \"MV Boli\";")
        self.label_process.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_process.setObjectName("label_process")

        self.advance = QtWidgets.QPushButton(self.centralwidget)
        self.advance.setGeometry(QtCore.QRect(30, 240, 101, 31))
        self.advance.setObjectName("advance")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(350, 240, 81, 31))
        self.start.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.start.setObjectName("start")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(420, 140, 42, 22))
        self.spinBox.setWrapping(True)
        self.spinBox.setFrame(True)
        self.spinBox.setAccelerated(True)
        self.spinBox.setProperty("showGroupSeparator", True)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.spinBox.setObjectName("spinBox")
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_speed.setGeometry(QtCore.QRect(370, 140, 41, 16))
        self.label_speed.setStyleSheet("")
        self.label_speed.setObjectName("label_speed")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 300, 51, 20))
        self.pushButton.setObjectName("pushButton")
        self.dockWidget_2 = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget_2.setGeometry(QtCore.QRect(10, 0, 301, 231))
        self.dockWidget_2.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(255, 255, 255);")
        self.dockWidget_2.setFloating(True)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 301, 211))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setAutoFillBackground(False)
        self.menu.setTearOffEnabled(False)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(False)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menu.addAction(self.actionNew)
        self.menubar.addAction(self.menu.menuAction())
        self.start.clicked.connect(self.start_main)
        self.retranslateUi(MainWindow)
        self.lineEdit_id.returnPressed.connect(self.label_process.clear)
        self.spinBox.valueChanged['QString'].connect(self.label_process.clear)
        self.lineEdit_id.textChanged['QString'].connect(self.label_process.setText)
        self.start.clicked.connect(self.label_process.clear)
        self.spinBox.valueChanged.connect(self.sleep)
        self.timeEdit_timing.timeChanged['QTime'].connect(self.label_process.clear)
        self.pushButton.clicked.connect(self.dockWidget_2.show)
        
        self.advance.clicked.connect(self.windowsec)
        self.advance.clicked.connect(MainWindow.hide)

        self.checkBox_chat.stateChanged.connect(self.chat)
        self.checkBox_audio.stateChanged.connect(self.audio)
        self.checkBox_video.stateChanged.connect(self.video)
        self.checkBox_join.stateChanged.connect(self.join)
        self.dockWidget_2.hide()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_info.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; color:#e3cf5a;\">By </span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">Suresh kumar</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">Contact :</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">EMAIL: sureshkumar3112001@gmail.com</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">Copy Rights :</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">The full copy Rights of the program is belong to developer team only</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">developer : Suresh Kumar.S </span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">Terms &amp; Conditions :</span></p><p><span style=\" font-size:10pt; color:#e3cf5a;\">This application is only use for educational surpose only and The developer is not responsible for any problem cause by this program or user actions</span></p></body></html>"))
        self.label_info.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#040404;\">Automated Google Meeting</span></p></body></html>"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "Entry Id Only"))
        self.label_id.setText(_translate("MainWindow", "Meeting Id :"))
        self.label_set_timing.setText(_translate("MainWindow", "Set Timinig :"))
        self.checkBox_join.setText(_translate("MainWindow", "Join"))
        self.checkBox_audio.setText(_translate("MainWindow", "Audio"))
        self.checkBox_video.setText(_translate("MainWindow", "Video"))
        self.checkBox_chat.setText(_translate("MainWindow", "Chat"))
        self.label_process.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.advance.setText(_translate("MainWindow", "Advance Options"))
        self.label_process.setText(_translate("MainWindow", "Enter id and timing is mandatory"))
        self.advance.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.label_speed.setText(_translate("MainWindow", "Speed :"))
        self.pushButton.setText(_translate("MainWindow", "About"))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "About"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">By </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">Suresh kumar</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">Contact :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">EMAIL: sureshkumar3112001@gmail.com</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">Copy Rights :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">The full copy Rights of the program is belong to developer team only</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">developer : Suresh Kumar.S </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">Terms &amp; Conditions :</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">This application is only use for educational surpose only and The developer is not responsible for any problem cause by this program or user actions</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    from app_2 import  Ui_Window2
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
