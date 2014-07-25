# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyString import *

class MyToolBar(QToolBar):
  def __init__(self, parent=None):
    super(MyToolBar,self).__init__(parent)
    self.setMovable(False)

    connButton = QToolButton(self)
    connButton.setIcon(QIcon("C:\\Users\\taco\\Documents\\GitHub\\PyQtConsole\\icons\\usb.png"))

    self.addWidget(connButton)
    self.setIconSize(QSize(48,48))
    