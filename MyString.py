# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MyString:
    @staticmethod
    def toUtf8(s):
        try:
            # return QString.fromUtf8(s)
            # return unicode(s, 'utf-8')
            return s
        except AttributeError:
            return s

    @staticmethod
    def translate(context, text):
        try:
            return QApplication.translate(context, text, None,
                                          QApplication.UnicodeUTF8)
        except AttributeError:
            return QApplication.translate(context, text, None)
