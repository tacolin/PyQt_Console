# -*- coding: utf-8 -*-

from serial import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyRecvEnd(Exception):
    def __init__(self):
        super(MyRecvEnd, self).__init__()


class MyRecv(QObject):

    recvData = pyqtSignal(str)

    def __init__(self, serial, rxbuf):
        super(MyRecv, self).__init__()
        self.serial = serial
        self.rxbuf = rxbuf
        self.isTerminated = True
        self.buf = ''
        self.maxBufSize = 1000
        self.checkList = []

    @pyqtSlot()
    def run(self):
        self.isTerminated = False
        firstByte = ''
        restDataLen = 0
        restBytes = ''
        try:
            while True and serial.isOpen():
                firstByte = serial.read()
                restDataLen = serial.inWaiting()
                if restDataLen > 0:
                    restBytes = serial.read(restDataLen)
                else:
                    restBytes = ''
                self.notifyRecvData(firstByte, restBytes)
                self.buf = ''.join([self.buf, firstByte, restBytes])
                self.fitBuf()
        except MyRecvEnd:
            self.isTerminated = True
            if self.serial.isOpen():
                self.serial.Close()
            self.buf = ''

    @pyqtSlot()
    def terminate(self):
        raise MyRecvEnd()

    def fitBuf(self):
        diff = len(self.buf) - self.maxBufSize
        if diff > 0:
            self.buf = self.buf[diff:]

    def notifyRecvData(self, *datas):
        for data in datas:
            self.recvData.emit(data)

    def checkBuf(self):
        for wait in self.checkList:
            pos = self.buf.find(wait['string'])
            if pos != -1:
                sig = pyqtSignal(bool)
                sig.connect(wait['slot'])
                sig.emit(True)
                pos = pos + len(wait['string'])
                self.buf = self.buf[pos:]

    def addWaitString(self, string, slot, timeout):
        self.checkList.append({'string': string, 'slot': slot})

    def isTerminated(self):
        return self.isTerminated


class MyConsole(QObject):
    def __init__(self, portName, textBrowser, waitTimeout=5):
        super(MyConsole, self).__init()
        self.portName = portName
        self.textBrowser = textBrowser
        try:
            self.serial = Serial(None, baudrate=115200, timeout=waitTimeout)
        except SerialException, e:
            raise e
