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

  def event(self,ev):
    if ev.type() == QEvent.KeyPress:
      if (ev.modifiers() & Qt.ControlModifier) and (Qt.Key_1 <= ev.key() <= Qt.Key_9) :
        print '[tabWidget] ctrl + 1~9'
      elif (ev.modifiers() & Qt.AltModifier) and (Qt.Key_1 <= ev.key() <= Qt.Key_9) :
        print '[tabWidget] alt + 1~9'
      elif (ev.modifiers() & Qt.ControlModifier) and (ev.key() == Qt.Key_PageUp or ev.key() == Qt.Key_PageDown) :
        print '[tabWidget] ctrl + page up/down'
      elif (ev.modifiers() & Qt.AltModifier) and (ev.key() == Qt.Key_PageUp or ev.key() == Qt.Key_PageDown) :
        print '[tabWidget] alt + page up/down'

    return super(MyTabWidget,self).event(ev)
