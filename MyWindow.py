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
        quitShortcut.activated.connect(self.closeWindowOnly)

    @pyqtSlot()
    def myClose(self):
        print('close MyWindow')

    @pyqtSlot()
    def closeWindowOnly(self):
        print('close window only')
        self.close()


if __name__ == '__main__':

    import sys
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    win = MyWindow()
    app.aboutToQuit.connect(win.myClose)

    win.show()

    sys.exit(app.exec_())
