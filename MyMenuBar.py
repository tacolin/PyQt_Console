 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *


try:
  _fromUtf8 = QString.fromUtf8
except AttributeError:
  def _fromUtf8(s):
    return s

try:
  _encoding = QApplication.UnicodeUTF8
  def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig)

class MyMenuBar(QMenuBar):
  def __init__(self,parent):
    super(MyMenuBar,self).__init__(parent)    
    self.fileMenu = self.addMenu(_fromUtf8('檔案(&F)'))