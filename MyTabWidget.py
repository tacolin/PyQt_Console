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

  # 為了讓 tab 上的叉叉按鈕，按下去以後真的會把 tab 關掉所做的
  @pyqtSlot(int)
  def closeTab(self,tabIndex):
    target = self.widget(tabIndex)
    self.removeTab(tabIndex)
    target.deleteLater()

    