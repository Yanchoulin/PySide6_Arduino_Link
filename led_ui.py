# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyside6_arduino_no2yLsKAP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_led_ui(object):
    def setupUi(self, led_ui):
        if not led_ui.objectName():
            led_ui.setObjectName(u"led_ui")
        led_ui.resize(887, 494)
        self.SW1 = QPushButton(led_ui)
        self.SW1.setObjectName(u"SW1")
        self.SW1.setGeometry(QRect(40, 250, 61, 51))
        self.pushButton_2 = QPushButton(led_ui)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 250, 61, 51))
        self.SW3 = QPushButton(led_ui)
        self.SW3.setObjectName(u"SW3")
        self.SW3.setGeometry(QRect(210, 250, 61, 51))
        self.SW4 = QPushButton(led_ui)
        self.SW4.setObjectName(u"SW4")
        self.SW4.setGeometry(QRect(290, 250, 61, 51))
        self.led1P = QPushButton(led_ui)
        self.led1P.setObjectName(u"led1P")
        self.led1P.setGeometry(QRect(40, 350, 131, 51))
        self.led2P = QPushButton(led_ui)
        self.led2P.setObjectName(u"led2P")
        self.led2P.setGeometry(QRect(210, 350, 141, 51))
        self.LD4P = QPushButton(led_ui)
        self.LD4P.setObjectName(u"LD4P")
        self.LD4P.setGeometry(QRect(120, 410, 61, 51))
        self.LD5P = QPushButton(led_ui)
        self.LD5P.setObjectName(u"LD5P")
        self.LD5P.setGeometry(QRect(210, 410, 61, 51))
        self.LD6P = QPushButton(led_ui)
        self.LD6P.setObjectName(u"LD6P")
        self.LD6P.setGeometry(QRect(290, 410, 61, 51))
        self.LD3P = QPushButton(led_ui)
        self.LD3P.setObjectName(u"LD3P")
        self.LD3P.setGeometry(QRect(40, 410, 61, 51))
        self.frame = QFrame(led_ui)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 30, 331, 181))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tempL = QLabel(self.frame)
        self.tempL.setObjectName(u"tempL")
        self.tempL.setGeometry(QRect(50, 100, 101, 51))
        font = QFont()
        font.setFamilies([u"DF7segHMI"])
        font.setPointSize(48)
        self.tempL.setFont(font)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 40, 311, 41))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 0, 111, 31))
        self.label_2.setFont(font1)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(170, 80, 151, 91))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.humiL = QLabel(self.frame_6)
        self.humiL.setObjectName(u"humiL")
        self.humiL.setGeometry(QRect(30, 20, 101, 51))
        self.humiL.setFont(font)
        self.humiL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 80, 161, 91))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 10, 141, 31))
        self.label_5.setFont(font1)
        self.frame_5.raise_()
        self.tempL.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.label_5.raise_()
        self.getdataP = QPushButton(led_ui)
        self.getdataP.setObjectName(u"getdataP")
        self.getdataP.setGeometry(QRect(400, 410, 141, 51))
        self.exitP = QPushButton(led_ui)
        self.exitP.setObjectName(u"exitP")
        self.exitP.setGeometry(QRect(700, 410, 141, 51))
        self.chargraph = QChartView(led_ui)
        self.chargraph.setObjectName(u"chargraph")
        self.chargraph.setGeometry(QRect(380, 30, 481, 341))
        self.frame_2 = QFrame(led_ui)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 210, 331, 101))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 0, 151, 31))
        self.label_3.setFont(font1)
        self.frame_3 = QFrame(led_ui)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 310, 331, 161))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 0, 171, 31))
        self.label_4.setFont(font1)
        self.frame_7 = QFrame(led_ui)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(380, 390, 481, 81))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.SW1.raise_()
        self.pushButton_2.raise_()
        self.SW3.raise_()
        self.SW4.raise_()
        self.led1P.raise_()
        self.led2P.raise_()
        self.LD4P.raise_()
        self.LD5P.raise_()
        self.LD6P.raise_()
        self.LD3P.raise_()
        self.frame.raise_()
        self.getdataP.raise_()
        self.exitP.raise_()
        self.chargraph.raise_()

        self.retranslateUi(led_ui)

        QMetaObject.connectSlotsByName(led_ui)
    # setupUi

    def retranslateUi(self, led_ui):
        led_ui.setWindowTitle(QCoreApplication.translate("led_ui", u"Form", None))
        self.SW1.setText(QCoreApplication.translate("led_ui", u"sw1", None))
        self.pushButton_2.setText(QCoreApplication.translate("led_ui", u"sw2", None))
        self.SW3.setText(QCoreApplication.translate("led_ui", u"sw3", None))
        self.SW4.setText(QCoreApplication.translate("led_ui", u"sw4", None))
        self.led1P.setText(QCoreApplication.translate("led_ui", u"LED1 ON", None))
        self.led2P.setText(QCoreApplication.translate("led_ui", u"LED2 ON", None))
        self.LD4P.setText(QCoreApplication.translate("led_ui", u"LED4", None))
        self.LD5P.setText(QCoreApplication.translate("led_ui", u"LED5", None))
        self.LD6P.setText(QCoreApplication.translate("led_ui", u"LED6", None))
        self.LD3P.setText(QCoreApplication.translate("led_ui", u"LED3", None))
        self.tempL.setText(QCoreApplication.translate("led_ui", u"20", None))
        self.label.setText(QCoreApplication.translate("led_ui", u"Temperature", None))
        self.label_2.setText(QCoreApplication.translate("led_ui", u"Humidity", None))
        self.humiL.setText(QCoreApplication.translate("led_ui", u"20", None))
        self.label_5.setText(QCoreApplication.translate("led_ui", u"Analogy In", None))
        self.getdataP.setText(QCoreApplication.translate("led_ui", u"Get Data", None))
        self.exitP.setText(QCoreApplication.translate("led_ui", u"Exit", None))
        self.label_3.setText(QCoreApplication.translate("led_ui", u"Digital Intput", None))
        self.label_4.setText(QCoreApplication.translate("led_ui", u"Digital Output", None))
    # retranslateUi







