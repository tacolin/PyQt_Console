# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyString import *

class MyStatusBar(QStatusBar):
  def __init__(self,parent=None):
    super(MyStatusBar,self).__init__(parent)

    self.showMessage(MyString.toUtf8('你好嗎？我不好'))
