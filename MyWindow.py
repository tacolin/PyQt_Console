 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyTabWidget import *


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

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.resize(800,600)
    self.setWindowTitle(_fromUtf8('Tacolin的視窗'))
    
    widget = QWidget(self)
    self.setCentralWidget(widget)  

    layout = QVBoxLayout(widget)
    tabWidget = MyTabWidget(widget)
    layout.addWidget(tabWidget)


if __name__ == '__main__':

  import sys
  import signal
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  app = QApplication(sys.argv)

  win = MyWindow()
  win.show()

  sys.exit( app.exec_() )
