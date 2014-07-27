# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MyTextBrowser(QTextBrowser):
    def __init__(self, parent):
        super(MyTextBrowser, self).__init__(parent)

    def event(self, ev):
        if ev.type() == QEvent.KeyPress:
            print(format(ev.key(), '02x'))
            if ev.key() == Qt.Key_Tab and ev.modifiers() == Qt.NoModifier:
                # 把單獨 tab 的 key press event 攔下來
                # 但像 alt + tab, ctrl + tab 要放行
                print('tab get')
                return True

        return super(MyTextBrowser, self).event(ev)
