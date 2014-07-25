# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyString import *

class MyTextEdit(QTextEdit):
  def __init__(self,parent=None):
    super(MyTextEdit,self).__init__(parent)

    self.setReadOnly(True)

  # 自己包過的 tab 內 widget，都要有一個 myClose 方法
  def myClose(self):
    self.deleteLater()

  def keyPressEvent(self,ev):
    print '[textEdit] key = {0}'.format(ev.key())

    # super(MyTextEdit,self).keyPressEvent(ev)
