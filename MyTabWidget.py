 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyTextBrowser import *
from MyString import *

class MyTabWidget(QTabWidget):
  def __init__(self,parent=None):
    super(MyTabWidget,self).__init__(parent)    

    tab1 = MyTextBrowser(self)
    self.addTab(tab1, MyString.toUtf8('測試用Tab1'))
    tab2 = MyTextBrowser(self)
    self.addTab(tab2, MyString.toUtf8('測試用Tab2'))

    self.setMovable(True)
    self.setTabsClosable(True)  