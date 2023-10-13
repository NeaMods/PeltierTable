#For the GUI
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QTimer
#from qtwidgets import Toggle
from toggleButton import Toggle
import numpy as np
from mecom import MeCom, ResponseException, WrongChecksum
from serial import SerialException
import serial.tools.list_ports
import pyqtgraph as pg
from datetime import datetime

# Import the generated Python module
from ui_heaterApp import Ui_MainWindow

# default queries from command table below
DEFAULT_QUERIES = [
    "loop status",
    "object temperature",
    "target object temperature",
    "output current",
    "output voltage"
]

# syntax
# { display_name: [parameter_id, unit], }
COMMAND_TABLE = {
    "loop status": [1200, ""],
    "object temperature": [1000, "degC"],
    "target object temperature": [1010, "degC"],
    "output current": [1020, "A"],
    "output voltage": [1021, "V"],
    "sink temperature": [1001, "degC"],
    "ramp temperature": [1011, "degC"],
}

class controlApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(controlApp,self).__init__()

        # Initialize the user interface from the generated module
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Temperature controller")

        self.ui.toggle_power = Toggle()
        self.ui.OffLabel = QtWidgets.QLabel("OFF")
        self.ui.OnLabel = QtWidgets.QLabel("ON")
        self.ui.TogglePlaceHolder.addWidget(self.ui.OffLabel)
        self.ui.TogglePlaceHolder.addWidget(self.ui.toggle_power)
        self.ui.TogglePlaceHolder.addWidget(self.ui.OnLabel)
        self.ui.toggle_power.toggled.connect(self.SwitchControl)

        #pyqtgraph settings
        self.styles = {'color':'b', 'font-size':'20px'}
        self.ui.PlotArea.setLabel('left', 'Temperature (°C)', **self.styles)
        self.ui.PlotArea.setBackground('w')
        axis = pg.DateAxisItem()
        self.ui.PlotArea.setAxisItems({'bottom':axis})
        self.ui.PlotArea.setLabel('bottom', 'Time', **self.styles)
        self.ui.PlotArea.showGrid(x=True, y=True)

        self.pen_Tplot = pg.mkPen(color=(0, 0, 0), width=5, style=QtCore.Qt.SolidLine)

        self.timer=QTimer(self)
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.timeout.connect(self.UpdateValues)

        self.ui.ResetButton.clicked.connect(self.ResetController)
        self.ui.SetPointButton.clicked.connect(self.SetTemperature)
        self.ui.radioButton_C.toggled.connect(self.TempSwitch)
        self.ui.radioButton_F.toggled.connect(self.TempSwitch)
        self.ui.radioButton_K.toggled.connect(self.TempSwitch)

        self.tempdata = np.array([])
        self.currentdata = []
        self.timedata = []
        self.tstart = []
        self.Npoints = 500

        self.ConnectToTEC()

    def ConnectToTEC(self):
        try:
            self.SearchCOMports()
            self.mc = MeerstetterTEC(port=self.deviceport)
            test = self.mc.get_data()
            self.loopflag = test['loop status'][0]
            self.ui.doubleSpinBox.setValue(test['target object temperature'][0])
            print(self.loopflag)
            if  self.loopflag:
                self.ui.toggle_power.setChecked(True)
            self.timer.start(250)
        except:
            print("No TEC controller connected")
            #self.NoTECfoundPopUp()

    def UpdateValues(self):
        dd = self.mc.get_data()

        T = (dd['object temperature'][0])
        self.tempdata = np.append(self.tempdata,T)
        if len(self.tempdata) > self.Npoints:
            self.tempdata = self.tempdata[1:]
        if self.ui.radioButton_C.isChecked():
            self.ui.lcdNumber_temp.display(T)
        elif self.ui.radioButton_F.isChecked():
            self.ui.lcdNumber_temp.display(T*9/5+32)
        elif self.ui.radioButton_K.isChecked():
            self.ui.lcdNumber_temp.display(T+273)

        C = dd['output current'][0]
        self.currentdata.append(C)
        if len(self.currentdata) > self.Npoints:
            self.currentdata = self.currentdata[1:]
        self.ui.lcdNumber_amp.display(C)

        #n = datetime.now()
        current_time = datetime.timestamp(datetime.now()) #n.strftime("%H:%M:%S")
        self.timedata.append(current_time)
        if len(self.timedata) > self.Npoints:
            self.timedata = self.timedata[1:]
        
        self.ui.PlotArea.clear()
        if self.ui.radioButton_C.isChecked():
            self.ui.PlotArea.plot(self.timedata,self.tempdata,pen=self.pen_Tplot)
        elif self.ui.radioButton_F.isChecked():
            self.ui.PlotArea.plot(self.timedata,self.tempdata*9/5+32,pen=self.pen_Tplot)
        elif self.ui.radioButton_K.isChecked():
            self.ui.PlotArea.plot(self.timedata,self.tempdata+273,pen=self.pen_Tplot)

    def ResetController(self):
        self.mc.resetting()

    def SetTemperature(self):
        v = self.ui.doubleSpinBox.value()
        if self.ui.radioButton_F.isChecked():
            self.mc.set_temp((v-32)*5/9)
        elif self.ui.radioButton_K.isChecked():
            self.mc.set_temp(v-273)
        else:
            self.mc.set_temp(v)

    def SwitchControl(self):
        if self.ui.toggle_power.isChecked():
            try:
                self.mc.enable()
            except:
                self.NoTECfoundPopUp()
        else:
            self.mc.disable()

    def TempSwitch(self):
        radioButton = self.sender()
        test = self.mc.get_data()
        v = test['target object temperature'][0]
        if radioButton.isChecked():
            if radioButton == self.ui.radioButton_C:
                self.ui.doubleSpinBox.setValue(v)
                self.ui.PlotArea.setLabel('left', 'Temperature (°C)', **self.styles)
            if radioButton == self.ui.radioButton_F:
                self.ui.doubleSpinBox.setValue(v*9/5+32)
                self.ui.PlotArea.setLabel('left', 'Temperature (F)', **self.styles)
            if radioButton == self.ui.radioButton_K:
                self.ui.doubleSpinBox.setValue(v+273)
                self.ui.PlotArea.setLabel('left', 'Temperature (K)', **self.styles)

    def SearchCOMports(self):
        comports = serial.tools.list_ports.comports()
        p = [x for x in comports if 'USB VID:PID=0403:6015 SER=DK0ADEVCA' in x.hwid]
        try:
            self.deviceport = p[0].name
            print(f"Device found on {self.deviceport}")
        except:
            print("No device was found")
            msg = QMessageBox(self)
            msg.setWindowTitle("No USB connection!")
            msg.setText("No USB connection found!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.setInformativeText("Connect the device to the PC!")
            button = msg.exec_()

            if button == QMessageBox.Ok:
                self.SearchCOMports()
            else:
                self.close()


    def NoTECfoundPopUp(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("No controller found")
        msg.setText("No TEC controller found!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText("Connect or turn the controller on, and relaunch app!")
        button = msg.exec_()

        if button == QMessageBox.Ok:
            self.close()

    def closeEvent(self, event):
        try:
            self.mc.disable()
        except:
            pass

class MeerstetterTEC(object):
    """
    Controlling TEC devices via serial.
    """

    def _tearDown(self):
        self.session().stop()

    def __init__(self, port="COM9", channel=1, queries=DEFAULT_QUERIES, *args, **kwars):
        assert channel in (1, 2)
        self.channel = channel
        self.port = port
        self.queries = queries
        self._session = None
        self._connect()

    def _connect(self):
        # open session
        self._session = MeCom(serialport=self.port)
        # get device address
        self.address = self._session.identify()
        print("connected to {}".format(self.address))

    def session(self):
        if self._session is None:
            self._connect()
        return self._session
    
    def resetting(self):
        self.session().reset_device()

    def get_data(self):
        data = {}
        for description in self.queries:
            id, unit = COMMAND_TABLE[description]
            try:
                value = self.session().get_parameter(parameter_id=id, address=self.address, parameter_instance=self.channel)
                data.update({description: (value, unit)})
            except (ResponseException, WrongChecksum) as ex:
                self.session().stop()
                self._session = None
        return data

    def set_temp(self, value):
        """
        Set object temperature of channel to desired value.
        :param value: float
        :param channel: int
        :return:
        """
        # assertion to explicitly enter floats
        assert type(value) is float
        print("set object temperature for channel {} to {} C".format(self.channel, value))
        return self.session().set_parameter(parameter_id=3000, value=value, address=self.address, parameter_instance=self.channel)

    def _set_enable(self, enable=True):
        """
        Enable or disable control loop
        :param enable: bool
        :param channel: int
        :return:
        """
        value, description = (1, "on") if enable else (0, "off")
        print("set loop for channel {} to {}".format(self.channel, description))
        return self.session().set_parameter(value=value, parameter_name="Status", address=self.address, parameter_instance=self.channel)

    def enable(self):
        return self._set_enable(True)

    def disable(self):
        return self._set_enable(False)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = controlApp()
    ex.show()
    sys.exit(app.exec_())