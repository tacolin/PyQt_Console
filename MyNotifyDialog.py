# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyNotifyDialog:
    @staticmethod
    def info(string):
        icon = QIcon('./icons/emoticon_smile.png')
        pixmap = icon.pixmap(48, 48)

        dialog = QDialog()
        dialog.setWindowTitle('INFO')
        dialog.setFont(QFont('Arial', 14))
        dialog.setWindowIcon(icon)

        picLabel = QLabel(dialog)
        picLabel.setPixmap(pixmap)
        picLabel.setContentsMargins(0, 10, 10, 10)

        textLabel = QLabel(string, dialog)
        textLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        textLabel.setWordWrap(True)

        infoWidget = QWidget(dialog)
        hlayout = QHBoxLayout(infoWidget)
        hlayout.addWidget(picLabel)
        hlayout.addWidget(textLabel)
        hlayout.addStretch()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, dialog)
        buttonBox.accepted.connect(dialog.accept)

        vlayout = QVBoxLayout(dialog)
        vlayout.addWidget(infoWidget)
        vlayout.addWidget(buttonBox)

        dialog.exec_()

    @staticmethod
    def warn(string):
        pass

    @staticmethod
    def error(string):
        pass

    @staticmethod
    def confirm(string):
        return True


if __name__ == '__main__':
    import sys
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)

    print('開始')
    MyNotifyDialog.info('當格數需要跨越多行時，就需要額外提供三個參數，例如 display 在第四橫列第一直行，因此第二個參數為 3 ，第三個參數為 0 ，第四個參數為垂直延伸格數，此處為 1 ，第五個參數為水平延伸格數，此處為 7')
    print('結束')
