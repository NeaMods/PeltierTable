# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'heaterApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 570)
        MainWindow.setStyleSheet(u"QMainWindow { \n"
"background-color: white \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PlotArea = PlotWidget(self.centralwidget)
        self.PlotArea.setObjectName(u"PlotArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotArea.sizePolicy().hasHeightForWidth())
        self.PlotArea.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.PlotArea)

        self.MenuFrame = QFrame(self.centralwidget)
        self.MenuFrame.setObjectName(u"MenuFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MenuFrame.sizePolicy().hasHeightForWidth())
        self.MenuFrame.setSizePolicy(sizePolicy1)
        self.MenuFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.MenuFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TogglePlaceHolder = QHBoxLayout()
        self.TogglePlaceHolder.setObjectName(u"TogglePlaceHolder")
        self.label_3 = QLabel(self.MenuFrame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.TogglePlaceHolder.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TogglePlaceHolder.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.TogglePlaceHolder)

        self.label_setpoint = QLabel(self.MenuFrame)
        self.label_setpoint.setObjectName(u"label_setpoint")
        self.label_setpoint.setFont(font)

        self.verticalLayout.addWidget(self.label_setpoint)

        self.doubleSpinBox = QDoubleSpinBox(self.MenuFrame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMinimum(5.000000000000000)
        self.doubleSpinBox.setMaximum(450.000000000000000)
        self.doubleSpinBox.setValue(24.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox)

        self.SetPointButton = QPushButton(self.MenuFrame)
        self.SetPointButton.setObjectName(u"SetPointButton")
        self.SetPointButton.setFont(font)

        self.verticalLayout.addWidget(self.SetPointButton)

        self.label_2 = QLabel(self.MenuFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_C = QRadioButton(self.MenuFrame)
        self.radioButton_C.setObjectName(u"radioButton_C")
        self.radioButton_C.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_C)

        self.radioButton_F = QRadioButton(self.MenuFrame)
        self.radioButton_F.setObjectName(u"radioButton_F")

        self.horizontalLayout.addWidget(self.radioButton_F)

        self.radioButton_K = QRadioButton(self.MenuFrame)
        self.radioButton_K.setObjectName(u"radioButton_K")

        self.horizontalLayout.addWidget(self.radioButton_K)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_temp = QLabel(self.MenuFrame)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setFont(font)

        self.verticalLayout.addWidget(self.label_temp)

        self.lcdNumber_temp = QLCDNumber(self.MenuFrame)
        self.lcdNumber_temp.setObjectName(u"lcdNumber_temp")
        self.lcdNumber_temp.setStyleSheet(u"QLCDNumber { \n"
"color: black; background-color: white \n"
"}")
        self.lcdNumber_temp.setFrameShape(QFrame.Shape.NoFrame)
        self.lcdNumber_temp.setSmallDecimalPoint(False)
        self.lcdNumber_temp.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_temp.setProperty("intValue", 0)

        self.verticalLayout.addWidget(self.lcdNumber_temp)

        self.label = QLabel(self.MenuFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lcdNumber_amp = QLCDNumber(self.MenuFrame)
        self.lcdNumber_amp.setObjectName(u"lcdNumber_amp")
        self.lcdNumber_amp.setStyleSheet(u"QLCDNumber { \n"
"color: black; background-color: white \n"
"}")
        self.lcdNumber_amp.setFrameShape(QFrame.Shape.NoFrame)
        self.lcdNumber_amp.setSmallDecimalPoint(False)
        self.lcdNumber_amp.setDigitCount(5)
        self.lcdNumber_amp.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout.addWidget(self.lcdNumber_amp)

        self.ResetButton = QPushButton(self.MenuFrame)
        self.ResetButton.setObjectName(u"ResetButton")

        self.verticalLayout.addWidget(self.ResetButton)


        self.horizontalLayout_2.addWidget(self.MenuFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.label_setpoint.setText(QCoreApplication.translate("MainWindow", u"Setpoint", None))
        self.SetPointButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Units", None))
        self.radioButton_C.setText(QCoreApplication.translate("MainWindow", u"\u00baC", None))
        self.radioButton_F.setText(QCoreApplication.translate("MainWindow", u"\u00baF", None))
        self.radioButton_K.setText(QCoreApplication.translate("MainWindow", u"\u00baK", None))
        self.label_temp.setText(QCoreApplication.translate("MainWindow", u"Current temperature", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.ResetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

