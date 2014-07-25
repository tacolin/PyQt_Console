# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyString import *

class MyTextEdit(QTextEdit):
  def __init__(self,parent=None):
    super(MyTextEdit,self).__init__(parent)

    self.setReadOnly(True)
