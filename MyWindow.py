# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from MyTabWidget import *
from MyToolBar import *
from MyStatusBar import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('Tacolin的視窗')

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)
        tabWidget = MyTabWidget(widget)
        layout.addWidget(tabWidget)

        toolBar = MyToolBar(self)
        self.addToolBar(toolBar)

        statusBar = MyStatusBar(self)
        self.setStatusBar(statusBar)

        quitShortcut = QShortcut(QKeySequence('Ctrl+Q'), self)
        quitShortcut.activated.connect(self.triggerClose)

    @pyqtSlot()
    def myClose(self):
        ''' 真正的結束程序 '''

        print("做一些必要的結束程序")

    @pyqtSlot()
    def triggerClose(self):
        ''' 只是觸發一個 close event 而已 '''

        self.close()

    @pyqtSlot()
    def closeEvent(self, ev):
        ''' 確認之後只會把視窗關閉  但真正的myClose會等到app quit才做 '''

        confirm = QMessageBox.question(self, '確認',
                                       '確定要關閉整個程式嗎？')
        if confirm == QMessageBox.Yes:
            ev.accept()
        else:
            ev.ignore()


if __name__ == '__main__':

    import sys
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    win = MyWindow()
    app.aboutToQuit.connect(win.myClose)

    win.show()

    sys.exit(app.exec_())
