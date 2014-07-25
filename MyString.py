# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyString:
  @staticmethod
  def toUtf8(s):
    try:
      return QString.fromUtf8(s)
    except AttributeError:
      return s

  @staticmethod
  def translate(context, text):
    try:
      return QApplication.translate(context, text, None, QApplication.UnicodeUTF8)
    except AttributeError:
      return QApplication.translate(context, text, None)
