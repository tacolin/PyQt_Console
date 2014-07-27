# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super(MyStatusBar, self).__init__(parent)
        self.showMessage('你好嗎？我不好')
