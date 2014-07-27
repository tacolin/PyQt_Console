# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from MyString import *


class MyToolBar(QToolBar):
    def __init__(self, parent=None):
        super(MyToolBar, self).__init__(parent)
        self.setMovable(False)

        connButton = QToolButton(self)
        connButton.setIcon(QIcon("./icons/usb.png"))

        self.addWidget(connButton)
        self.setIconSize(QSize(48, 48))
