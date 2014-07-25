 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyTextBrowser import *
from MyTextEdit import *
from MyString import *

class MyTabWidget(QTabWidget):
  def __init__(self,parent=None):
    super(MyTabWidget,self).__init__(parent)    

    tab1 = MyTextEdit(self)
    self.addTab(tab1, MyString.toUtf8('測試用Tab1'))
    tab2 = MyTextEdit(self)
    self.addTab(tab2, MyString.toUtf8('測試用Tab2'))

    self.setMovable(True)

    # 為了讓 tab 上的叉叉按鈕，按下去以後真的會把 tab 關掉所做的
    self.setTabsClosable(True)
    self.tabCloseRequested.connect(self.closeTab)

    closeTabShortcut = QShortcut(QKeySequence('Ctrl+W'), self)
    closeTabShortcut.activated.connect(self.closeFocusedTab)

  # 為了讓 tab 上的叉叉按鈕，按下去以後真的會把 tab 關掉所做的
  @pyqtSlot(int)
  def closeTab(self,tabIndex):    
    if tabIndex < 0: # tabIndex 最小是 0
      return

    target = self.widget(tabIndex)
    self.removeTab(tabIndex)    
    target.myClose() # 自己包過的 tab 內 widget，都要有一個 myClose 方法

  @pyqtSlot()
  def closeFocusedTab(self):
    tabIndex = self.currentIndex()
    if tabIndex >= 0: # tabIndex 最小是 0
      self.closeTab(tabIndex)

  def keyPressEvent(self,ev):
    print '[tabWidget] key = {0}'.format(ev.key())