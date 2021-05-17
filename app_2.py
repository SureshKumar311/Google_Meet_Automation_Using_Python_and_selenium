
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from selenium import*
from selenium import webdriver
import os
from time import sleep
import datetime as dt
from datetime import datetime
import time

from app_1 import  Ui_MainWindow


class Ui_Window2(object):
    def normal1(self):
        # exit(0)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    global chatv
    global joinv
    global videov
    global audiov
    global speedv
    global chatv_2
    def callend (self):
        self.browser.find_element_by_css_selector(".GaONte").click()


    def end1(self):
        self.ch =self.checkBox_chat_2.checkState()
        if (self.ch==2):
            self.label_process.setText("end is Enabled")
            self.chatv_2 = 1
        else :
            self.label_process.setText("end is disabled")
            self.chatv_2 = 0

    def sleep(self):
        self.s=self.spinBox_speed.value()
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
            self.n=self.timeEdit_start.time() #geting window timnig
            add_timing=(self.n.addSecs(50).toString(Qt.ISODate)) ## add of timinig to lable
            add_timing_end1=(self.n.addSecs(3600).toString(Qt.ISODate))

            ch_la =self.timeEdit_ch_last.time()
            add_timing_la=(ch_la.addSecs(50).toString(Qt.ISODate))

            ch_ft =self.timeEdit_ch_first.time()
            add_timing_ft=(ch_ft.addSecs(50).toString(Qt.ISODate))

            ch_en =self.timeEdit_ch_first.time()
            add_timing_en=(ch_en.addSecs(50).toString(Qt.ISODate))

            current_timing=QTime.currentTime() ###current timig
            timig_org=(current_timing.toString()) ### cuting milisecond

            # print (timig_org)
            print(add_timing)

            # print (self.chatv)
            # print (self.videov)
            # print (self.audiov)

            # print (self.joinv)
            # print (self.speedv)
            # print(self.chatv_2)
            # self.a="https://meet.google.com/wbn-zbnx-csc"
            
     
            # print(add_timing_ft)
            # print(add_timing_la)
            # print(add_timing_en)

            start_time = timig_org
            # seconds = 4

            print(start_time)
            while True:

                # if(add_timing >= start_time):
                #     print ("hdsj" )

                # #print((int(elapsed_time)): 

                # if (elapsed_time > 2323):
                #     print("wor")
                    #print("Finished iterating in: " + str(int(elapsed_time))  

            # tim =(int(timig_org) - add_timing)
            # print(tim)
            # for i in range(tim):
            #     nnnnnnnnnnpritn("ij timing sk")

            # sleep(5)
            # exit(0)
            # exit(0)
            # # print (dt.datetime.now().hour)
            # # print  (dt.datetime.now().minute)

            # # current_hour = dt.datetime.now().hour
            # # current_min = dt.datetime.now().minute
            # for i in range(1):


            # if (timig_org==add_timing):

                print("hi")
                self.url=self.lineEdit_id.text()
                #self.a =("https://meet.google.com/"+str(self.url))
                self.a="https://meet.google.com/wbn-zbnx-csc"

                self.ch_first=self.lineEdit_chfirst.text()
                self.ch_last=self.lineEdit_chlast.text()


                self.browser = webdriver.Firefox("C:\\Users\\sk\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\i39cxzmn.sk")
                self.browser.get(self.a)
                sleep(self.speedv)
                if (self.audiov==0):
                    self.browser.find_element_by_class_name ("DPvwYc").click()

                if (self.videov==0):
                    self.browser.find_element_by_class_name("I5fjHe").click()
                    

                if (self.joinv==1):
                    self.browser.find_element_by_class_name("NPEfkd").click()

                    while (add_timing >= start_time):
                        
                        if (self.chatv==1):
                            while (add_timing):
                                                      
                                                                                    
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys(self.ch_last)
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span").click()
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button").click()

                        if (timig_org==add_timing_ft):
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys(self.ch_first)
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span/span/span").click()
                                self.browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button").click()
                                # callend()

                    #     if (self.chatv_2==1):
                    #         for i in range(add_timing):
                    #             if (timig_org==add_timing_en):
                    #                 callend()
                    # for i in range(add_timing_en):

                   
                    #     if (self.chatv==1):
                    #         for i in range(add_timing_end1):    
                       
                    #     if (self.chatv_2==1):
                    #         if (timig_org==add_timing_en):
                    #             self.browser.find_element_by_css_selector(".GaONte").click()
                    #             exit(0)


    def setupUi(self, Window2):
        self.chatv =0
        self.joinv=0
        self.videov=0
        self.audiov=0
        self.speedv=2
        self.end=0
        self.chatv_2=0
            
        Window2.setObjectName("Window2")
        Window2.setWindowModality(QtCore.Qt.NonModal)
        Window2.resize(479, 433)
        Window2.setStyleSheet("background-color: rgb(48, 200, 255);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Window2)
        self.buttonBox.setGeometry(QtCore.QRect(10, 600, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_info = QtWidgets.QLabel(Window2)
        self.label_info.setGeometry(QtCore.QRect(10, 30, 451, 41))
        self.label_info.setStyleSheet("font: 14pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(229, 229, 68);")
        self.label_info.setObjectName("label_info")
        self.checkBox_video = QtWidgets.QCheckBox(Window2)
        self.checkBox_video.setGeometry(QtCore.QRect(340, 140, 51, 17))
        self.checkBox_video.setObjectName("checkBox_video")
        self.label_starttiming = QtWidgets.QLabel(Window2)
        self.label_starttiming.setGeometry(QtCore.QRect(20, 300, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_starttiming.setFont(font)
        self.label_starttiming.setObjectName("label_starttiming")
        self.lineEdit_id = QtWidgets.QLineEdit(Window2)
        self.lineEdit_id.setGeometry(QtCore.QRect(110, 100, 171, 31))
        self.lineEdit_id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_id.setDragEnabled(True)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_id = QtWidgets.QLabel(Window2)
        self.label_id.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_process = QtWidgets.QLabel(Window2)
        self.label_process.setGeometry(QtCore.QRect(140, 350, 201, 51))
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
        self.label_process.setStyleSheet("background-color: rgb(236, 211, 18);\n"
"font: 9pt \"MV Boli\";")
        self.label_process.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_process.setWordWrap(True)
        self.label_process.setObjectName("label_process")
        self.checkBox_audio = QtWidgets.QCheckBox(Window2)
        self.checkBox_audio.setGeometry(QtCore.QRect(340, 90, 51, 21))
        self.checkBox_audio.setChecked(False)
        self.checkBox_audio.setObjectName("checkBox_audio")
        self.normal = QtWidgets.QPushButton(Window2)
        self.normal.setGeometry(QtCore.QRect(20, 360, 101, 31))
        palette = QtGui.QPalette()
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QConicalGradient(0.0, 0.0, 135.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.375, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(0.423533, QtGui.QColor(251, 255, 0, 145))
        gradient.setColorAt(0.45, QtGui.QColor(247, 255, 0, 208))
        gradient.setColorAt(0.477581, QtGui.QColor(255, 244, 71, 130))
        gradient.setColorAt(0.518717, QtGui.QColor(255, 218, 71, 130))
        gradient.setColorAt(0.55, QtGui.QColor(255, 255, 0))
        gradient.setColorAt(0.57754, QtGui.QColor(255, 203, 0, 130))
        gradient.setColorAt(0.625, QtGui.QColor(255, 255, 0, 69))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 0, 69))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.normal.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.normal.setFont(font)
        self.normal.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.normal.setObjectName("normal")
        self.start = QtWidgets.QPushButton(Window2)
        self.start.setGeometry(QtCore.QRect(370, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.start.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.start.setObjectName("start")
        self.checkBox_join = QtWidgets.QCheckBox(Window2)
        self.checkBox_join.setGeometry(QtCore.QRect(410, 90, 41, 21))
        self.checkBox_join.setChecked(False)
        self.checkBox_join.setObjectName("checkBox_join")
        self.checkBox_chat = QtWidgets.QCheckBox(Window2)
        self.checkBox_chat.setGeometry(QtCore.QRect(410, 140, 41, 20))
        self.checkBox_chat.setTristate(False)
        self.checkBox_chat.setObjectName("checkBox_chat")

        self.timeEdit_start = QtWidgets.QTimeEdit(Window2)
        self.timeEdit_start.setGeometry(QtCore.QRect(110, 290, 131, 31))
        self.timeEdit_start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_start.setAccelerated(True)
        self.timeEdit_start.setCalendarPopup(False)
        self.timeEdit_start.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit_start.setObjectName("timeEdit_start")
        self.lineEdit_chfirst = QtWidgets.QLineEdit(Window2)
        self.lineEdit_chfirst.setGeometry(QtCore.QRect(110, 150, 141, 51))
        self.lineEdit_chfirst.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_chfirst.setDragEnabled(True)
        self.lineEdit_chfirst.setReadOnly(True)
        self.lineEdit_chfirst.setObjectName("lineEdit_chfirst")
        self.lineEdit_chlast = QtWidgets.QLineEdit(Window2)
        self.lineEdit_chlast.setGeometry(QtCore.QRect(110, 220, 141, 51))
        self.lineEdit_chlast.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_chlast.setDragEnabled(True)
        self.lineEdit_chlast.setReadOnly(True)
        self.lineEdit_chlast.setObjectName("lineEdit_chlast")
        self.label_chfirst = QtWidgets.QLabel(Window2)
        self.label_chfirst.setGeometry(QtCore.QRect(30, 170, 61, 21))
        self.label_chfirst.setObjectName("label_chfirst")
        self.label_chlast = QtWidgets.QLabel(Window2)
        self.label_chlast.setGeometry(QtCore.QRect(30, 240, 61, 16))
        self.label_chlast.setObjectName("label_chlast")
        self.timeEdit_last = QtWidgets.QTimeEdit(Window2)
        self.timeEdit_last.setGeometry(QtCore.QRect(340, 290, 131, 31))
        self.timeEdit_last.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_last.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit_last.setObjectName("timeEdit_last")
        self.timeEdit_last.hide()
        self.label_endstiming = QtWidgets.QLabel(Window2)
        self.label_endstiming.setGeometry(QtCore.QRect(250, 300, 81, 21))
        self.label_endstiming.hide()
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_endstiming.setFont(font)
        self.label_endstiming.setObjectName("label_endstiming")
        self.timeEdit_ch_first = QtWidgets.QTimeEdit(Window2)
        self.timeEdit_ch_first.setGeometry(QtCore.QRect(370, 210, 71, 21))
        self.timeEdit_ch_first.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_ch_first.setWrapping(True)
        self.timeEdit_ch_first.setAccelerated(True)
        self.timeEdit_ch_first.setObjectName("timeEdit_ch_first")

        self.timeEdit_ch_last = QtWidgets.QTimeEdit(Window2)
        self.timeEdit_ch_last.setGeometry(QtCore.QRect(370, 240, 71, 21))
        self.timeEdit_ch_last.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit_ch_last.setWrapping(True)
        self.timeEdit_ch_last.setAccelerated(True)
        self.timeEdit_ch_last.setObjectName("timeEdit_ch_last")
        self.timeEdit_ch_last.hide()
        self.timeEdit_ch_first.hide()
        self.label_chatlast = QtWidgets.QLabel(Window2)
        self.label_chatlast.setGeometry(QtCore.QRect(270, 240, 91, 16))
        self.label_chatlast.setObjectName("label_chatlast")
        self.label_chatfast = QtWidgets.QLabel(Window2)
        self.label_chatfast.setGeometry(QtCore.QRect(270, 210, 91, 21))
        self.label_chatfast.setObjectName("label_chatfast")
        self.label_chatfast.hide()
        self.label_chatlast.hide()
        self.spinBox_speed = QtWidgets.QSpinBox(Window2)
        self.spinBox_speed.setGeometry(QtCore.QRect(400, 170, 42, 22))
        self.spinBox_speed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_speed.setWrapping(True)
        self.spinBox_speed.setFrame(True)
        self.spinBox_speed.setAccelerated(True)
        self.spinBox_speed.setProperty("showGroupSeparator", True)
        self.spinBox_speed.setMinimum(1)
        self.spinBox_speed.setMaximum(3)
        self.spinBox_speed.setObjectName("spinBox_speed")
        self.label_speed = QtWidgets.QLabel(Window2)
        self.label_speed.setGeometry(QtCore.QRect(340, 170, 51, 20))
        self.label_speed.setStyleSheet("")
        self.label_speed.setObjectName("label_speed")
        self.checkBox_chat_2 = QtWidgets.QCheckBox(Window2)
        self.checkBox_chat_2.setGeometry(QtCore.QRect(290, 140, 41, 20))
        self.checkBox_chat_2.setObjectName("checkBox_chat_2")
        self.dockWidget_2 = QtWidgets.QDockWidget(Window2)
        self.dockWidget_2.setGeometry(QtCore.QRect(90, 80, 301, 231))
        self.dockWidget_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.dockWidget_2.setFloating(True)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 301, 211))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.dockWidget_2.hide()
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.pushButton = QtWidgets.QPushButton(Window2)
        self.pushButton.setGeometry(QtCore.QRect(200, 410, 51, 20))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Window2)
        self.lineEdit_id.returnPressed.connect(self.label_process.clear)
        self.lineEdit_chfirst.textChanged['QString'].connect(self.label_process.setText)
        self.lineEdit_id.textChanged['QString'].connect(self.label_process.setText)
        self.lineEdit_chlast.textEdited['QString'].connect(self.label_process.setText)
        self.lineEdit_chfirst.returnPressed.connect(self.label_process.clear)
        self.lineEdit_chlast.returnPressed.connect(self.label_process.clear)
        self.checkBox_chat_2.clicked.connect(self.timeEdit_last.show)
        self.checkBox_chat_2.clicked.connect(self.label_endstiming.show)

        self.checkBox_chat.clicked.connect(lambda :self.lineEdit_chfirst.setReadOnly(False))
        self.checkBox_chat.clicked.connect(lambda :self.lineEdit_chlast.setReadOnly(False))
        self.checkBox_chat.clicked.connect(self.timeEdit_ch_first.show)
        self.checkBox_chat.clicked.connect(self.timeEdit_ch_last.show)

        self.timeEdit_start.timeChanged['QTime'].connect(self.label_process.clear)
        self.normal.clicked.connect(Window2.close)
        self.normal.clicked.connect(self.normal1)

        self.start.clicked.connect(self.label_process.clear)
        self.spinBox_speed.valueChanged['int'].connect(self.label_process.setNum)
        
        self.checkBox_chat.clicked.connect(self.label_chatfast.show)
        self.checkBox_chat.clicked.connect(self.label_chatlast.show)
        self.pushButton.clicked.connect(self.dockWidget_2.show)
        self.start.clicked.connect(self.start_main)
        self.checkBox_chat.stateChanged.connect(self.chat)
        self.checkBox_audio.stateChanged.connect(self.audio)
        self.checkBox_video.stateChanged.connect(self.video)
        self.checkBox_join.stateChanged.connect(self.join)
        self.checkBox_chat_2.stateChanged.connect(self.end1)
        QtCore.QMetaObject.connectSlotsByName(Window2)
        self.spinBox_speed.valueChanged.connect(self.sleep)


    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Window"))
        self.label_info.setText(_translate("Window2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#040404;\">Automated Google Meeting Advance</span></p></body></html>"))
        self.checkBox_video.setText(_translate("Window2", "Video"))
        self.label_starttiming.setText(_translate("Window2", "Start Timinig :"))
        self.lineEdit_id.setPlaceholderText(_translate("Window2", "Entry Id Only"))
        self.label_id.setText(_translate("Window2", "Meeting Id :"))
        self.label_process.setText(_translate("Window2", "id and start timing is mandatory"))
        self.checkBox_audio.setText(_translate("Window2", "Audio"))
        self.normal.setText(_translate("Window2", " Close "))
        self.normal.setShortcut(_translate("Window2", "Ctrl+N"))
        self.start.setText(_translate("Window2", "Start"))
        self.checkBox_join.setText(_translate("Window2", "Join"))
        self.checkBox_chat.setText(_translate("Window2", "Chat"))
        self.label_chfirst.setText(_translate("Window2", "Chat_First :"))
        self.label_chlast.setText(_translate("Window2", "Chat_last :"))
        self.label_endstiming.setText(_translate("Window2", "End Timinig :"))
        self.label_chatlast.setText(_translate("Window2", "Chat_last_Timing : :"))
        self.label_chatfast.setText(_translate("Window2", "Chat_First_timing :"))
        self.label_speed.setText(_translate("Window2", "Speed :"))
        self.checkBox_chat_2.setText(_translate("Window2", "End"))
        self.dockWidget_2.setWindowTitle(_translate("Window2", "About"))
        self.textBrowser.setHtml(_translate("Window2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
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
        self.pushButton.setText(_translate("Window2", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2 = QtWidgets.QDialog()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    Window2.show()
    sys.exit(app.exec_())
