 # -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MyString import *


class MyMenuBar(QMenuBar):
  def __init__(self,parent):
    super(MyMenuBar,self).__init__(parent)    
    self.fileMenu = self.addMenu(MyString.toUtf8('檔案(&F)'))