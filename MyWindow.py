 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyTabWidget import *
# from MyMenuBar import *
from MyToolBar import *
from MyString import *

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.resize(800,600)
    self.setWindowTitle(MyString.toUtf8('Tacolin的視窗'))
    
    widget = QWidget(self)
    self.setCentralWidget(widget)  

    layout = QVBoxLayout(widget)
    tabWidget = MyTabWidget(widget)
    layout.addWidget(tabWidget)

    # menuBar = MyMenuBar(self)
    # self.setMenuBar(menuBar)
    toolBar = MyToolBar(self)
    self.addToolBar(toolBar)


if __name__ == '__main__':

  import sys
  import signal
  signal.signal(signal.SIGINT, signal.SIG_DFL)

  app = QApplication(sys.argv)

  win = MyWindow()
  win.show()

  sys.exit( app.exec_() )
