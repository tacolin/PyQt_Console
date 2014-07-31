# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSerialPort import *


class MyVt100(QObject):
    """用來處理vt100及ascii code的部分"""

    LUMINACE_1 = 1
    LUMINACE_2 = 2
    LUMINACE_3 = 3
    LUMINACE_4 = 4
    LUMINACE_5 = 5

    TEXT_BLACK = 30
    TEXT_RED = 31
    TEXT_GREEN = 32
    TEXT_YELLOW = 33
    TEXT_BLUE = 34
    TEXT_PURPLE = 35
    TEXT_CYAN = 36
    TEXT_WHITE = 37

    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_PURPLE = 45
    BG_CYAN = 46
    BG_WHITE = 47

    CURSOR_RIGHT = 100
    CURSOR_LEFT = 200

    def __init__(self):
        super(MyVt100, self).__init__()

    def configSignal(self):
        self.cursorMoved = pyqtSignal(int, int)
        self.textAppend = pyqtSignal(str)
        self.textColorChanged = pyqtSignal(int, str)
        self.backgroundColorChanged = pyqtSignal(int, str)

    @pyqtSlot(bytes)
    def handleData(self, bytes):
        pass
