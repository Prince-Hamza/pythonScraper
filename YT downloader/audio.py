import threading
from pytube import YouTube

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QRect,Qt, QTimer)
from PyQt5.QtGui import (QFont)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import time, os
import threading
dir = os.getcwd()

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(450, 201)
        ProgressBar.setStyleSheet(u"background-color: rgb(54, 57, 63);")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressBar.sizePolicy().hasHeightForWidth())
        ProgressBar.setSizePolicy(sizePolicy)
        ProgressBar.setWindowOpacity(1.500000)
        self.groupBox = QGroupBox(ProgressBar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 410, 121))
        self.groupBox.setStyleSheet(u"background-color: rgb(47, 49, 54);\n"
"border: 1px solid black;\n"
"border-color: rgb(41, 43, 47);\n"
"border-radius: 7px;")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 80, 370, 21))
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 15px;\n"
"}")
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 370, 20))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: .5px solid black;\n"
"border-color: rgb(41, 43, 47);\n"
"border-radius: 2px;\n"
"color: white;")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 260, 20))
        self.label_2.setStyleSheet(u"border: .5px solid black;\n"
"border-color: rgb(41, 43, 47);\n"
"border-radius: 2px;\n"
"color: white;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(305, 50, 95, 20))
        self.label_3.setStyleSheet(u"border: .5px solid black;\n"
"border-color: rgb(41, 43, 47);\n"
"border-radius: 2px;\n"
"color: white;")

        self.retranslateUi(ProgressBar)
        QMetaObject.connectSlotsByName(ProgressBar)
        self.thr = threading.Thread(target=self.func).start()
        time.sleep(20)

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"Download Progress", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("ProgressBar", u"title", None))
        self.label_2.setText(QCoreApplication.translate("ProgressBar", u"url", None))
        self.label_3.setText(QCoreApplication.translate("ProgressBar", u"resolution", None))
    

    def func(self):
        with open(dir + "\\history.dat", 'r') as f:
            line = f.readlines()[-1]
            n = line.split('`')
            title = n[0]
            url = n[1]
            r = n[2]
        yt = YouTube(url, on_progress_callback=self.progress_func)
        self.label.setText(title)
        self.label_2.setText(url)
        self.label_3.setText("Resolution" + r)
        stream = yt.streams.get_by_itag(251)
        stream.download(filename="aud.webm" , skip_existing=False)

            
    def progress_func(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        self.progress = (float(abs(bytes_remaining-size)/size))*float(100)
        self.progressBar.setValue(int(self.progress))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    Dialog = QtWidgets.QDialog()
    ui = Ui_ProgressBar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())