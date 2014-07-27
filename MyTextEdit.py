# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from MyString import *


class MyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(MyTextEdit, self).__init__(parent)

        self.setReadOnly(True)

    # 自己包過的 tab 內 widget，都要有一個 myClose 方法
    def myClose(self):
        self.deleteLater()

    def event(self, ev):
        if ev.type() == QEvent.KeyPress:
            print('[textEdit 2] key = {0}'.format(ev.key()))
            if ev.key() == Qt.Key_Tab and ev.modifiers() == Qt.NoModifier:
                # 把 單純 tab 鍵的 event 截下來
                print('pure tab catched')
                return True

        return super(MyTextEdit, self).event(ev)
