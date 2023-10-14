# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'heaterApp.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1108, 607)
        MainWindow.setStyleSheet(u"QMainWindow { \n"
"background-color: white \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.PlotArea = PlotWidget(self.centralwidget)
        self.PlotArea.setObjectName(u"PlotArea")
        self.PlotArea.setGeometry(QRect(29, 10, 841, 561))
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(890, 100, 201, 31))
        font = QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMinimum(5.000000000000000)
        self.doubleSpinBox.setMaximum(450.000000000000000)
        self.doubleSpinBox.setValue(24.000000000000000)
        self.SetPointButton = QPushButton(self.centralwidget)
        self.SetPointButton.setObjectName(u"SetPointButton")
        self.SetPointButton.setGeometry(QRect(890, 140, 201, 41))
        self.SetPointButton.setFont(font)
        self.label_setpoint = QLabel(self.centralwidget)
        self.label_setpoint.setObjectName(u"label_setpoint")
        self.label_setpoint.setGeometry(QRect(890, 65, 201, 31))
        self.label_setpoint.setFont(font)
        self.lcdNumber_temp = QLCDNumber(self.centralwidget)
        self.lcdNumber_temp.setObjectName(u"lcdNumber_temp")
        self.lcdNumber_temp.setGeometry(QRect(890, 350, 201, 41))
        self.lcdNumber_temp.setStyleSheet(u"QLCDNumber { \n"
"color: black; background-color: white \n"
"}")
        self.lcdNumber_temp.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_temp.setSmallDecimalPoint(False)
        self.lcdNumber_temp.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber_temp.setProperty("intValue", 0)
        self.label_temp = QLabel(self.centralwidget)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setGeometry(QRect(890, 315, 191, 31))
        self.label_temp.setFont(font)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(890, 20, 201, 41))
        self.TogglePlaceHolder = QHBoxLayout(self.horizontalLayoutWidget)
        self.TogglePlaceHolder.setObjectName(u"TogglePlaceHolder")
        self.TogglePlaceHolder.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.TogglePlaceHolder.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.TogglePlaceHolder.addItem(self.horizontalSpacer)

        self.lcdNumber_amp = QLCDNumber(self.centralwidget)
        self.lcdNumber_amp.setObjectName(u"lcdNumber_amp")
        self.lcdNumber_amp.setGeometry(QRect(890, 440, 201, 41))
        self.lcdNumber_amp.setStyleSheet(u"QLCDNumber { \n"
"color: black; background-color: white \n"
"}")
        self.lcdNumber_amp.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_amp.setSmallDecimalPoint(False)
        self.lcdNumber_amp.setDigitCount(5)
        self.lcdNumber_amp.setSegmentStyle(QLCDNumber.Flat)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(890, 410, 191, 21))
        self.label.setFont(font)
        self.ResetButton = QPushButton(self.centralwidget)
        self.ResetButton.setObjectName(u"ResetButton")
        self.ResetButton.setGeometry(QRect(890, 530, 201, 41))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(890, 210, 201, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_C = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_C.setObjectName(u"radioButton_C")
        self.radioButton_C.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_C)

        self.radioButton_F = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_F.setObjectName(u"radioButton_F")

        self.horizontalLayout.addWidget(self.radioButton_F)

        self.radioButton_K = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_K.setObjectName(u"radioButton_K")

        self.horizontalLayout.addWidget(self.radioButton_K)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(890, 190, 55, 16))
        self.label_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SetPointButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_setpoint.setText(QCoreApplication.translate("MainWindow", u"Setpoint", None))
        self.label_temp.setText(QCoreApplication.translate("MainWindow", u"Current temperature", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.ResetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.radioButton_C.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.radioButton_F.setText(QCoreApplication.translate("MainWindow", u"\u00baF", None))
        self.radioButton_K.setText(QCoreApplication.translate("MainWindow", u"\u00baK", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Units", None))
    # retranslateUi

