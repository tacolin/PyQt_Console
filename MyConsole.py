# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSerialPort import *


class MySerialPort(QSerialPort):
    def __init__(self, parent=None):
        super(MySerialPort, self).__init__(parent)


def showAvailablePorts():
    for port in QSerialPortInfo.availablePorts():
        print('name {0}, desc {1}, serialNo. {2}, '
              'location {3}, busy {4}'.format(port.portName(),
                                              port.description(),
                                              port.serialNumber(),
                                              port.systemLocation(),
                                              port.isBusy()
                                              )
              )

if __name__ == '__main__':

    serial = MySerialPort()
    serial.setPortName('COM20')
    serial.setBaudRate(QSerialPort.Baud115200)
    serial.setFlowControl(QSerialPort.NoFlowControl)

    if serial.open(QIODevice.ReadWrite) is True:
        print('開啟成功')
        serial.close()
        print('關閉')
    else:
        print('開啟失敗, 原因:{0}'.format(serial.error()))

    print('去你的')
