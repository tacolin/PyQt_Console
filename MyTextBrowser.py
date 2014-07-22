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

class MyTextBrowser(QTextBrowser):
  def __init__(self,parent):
    super(MyTextBrowser,self).__init__(parent)

  def event(self,ev):
    if ev.type() == QEvent.KeyPress:
      print format(ev.key(),'02x')
      if ev.key() == Qt.Key_Tab:
        return True # 把 event 攔下來

    return super(MyTextBrowser,self).event(ev)

  # def keyPressEvent(self,ev):
  #   print format(ev.key(),'02x')
