# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyNotifyDialog(QDialog):
    def __init__(self, string, title, icon, buttonBoxType, parent=None):
        super(MyNotifyDialog, self).__init__(parent)
        pixmap = icon.pixmap(48, 48)

        self.setWindowTitle(title)
        self.setFont(QFont('Arial', 14))
        self.setWindowIcon(icon)

        picLabel = QLabel(self)
        picLabel.setPixmap(pixmap)
        picLabel.setContentsMargins(0, 10, 10, 10)

        textLabel = QLabel(string, self)
        textLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        textLabel.setWordWrap(True)

        infoWidget = QWidget(self)
        hlayout = QHBoxLayout(infoWidget)
        hlayout.addWidget(picLabel)
        hlayout.addWidget(textLabel)
        hlayout.addStretch()

        buttonBox = QDialogButtonBox(buttonBoxType, self)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        vlayout = QVBoxLayout(self)
        vlayout.addWidget(infoWidget)
        vlayout.addWidget(buttonBox)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    @staticmethod
    def info(string):
        icon = QIcon('./icons/emoticon_smile.png')
        dialog = MyNotifyDialog(string, 'INFO', icon, QDialogButtonBox.Ok)
        return dialog.exec_()

    @staticmethod
    def warn(string):
        icon = QIcon('./icons/emoticon_confused.png')
        dialog = MyNotifyDialog(string, 'WARNING', icon, QDialogButtonBox.Ok)
        return dialog.exec_()

    @staticmethod
    def error(string):
        icon = QIcon('./icons/emoticon_angry.png')
        dialog = MyNotifyDialog(string, 'ERROR', icon, QDialogButtonBox.Ok)
        return dialog.exec_()

    @staticmethod
    def confirm(string):
        icon = QIcon('./icons/help2.png')
        dialog = MyNotifyDialog(string, 'CONFIRM', icon,
                                QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        return dialog.exec_()


if __name__ == '__main__':
    import sys
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)

    longMessage = ('當格數需要跨越多行時，就需要額外提供三個參數，例如 display'
                   '當在第四橫列第一直行，因此第二個參數為 3，第三個參數為 0，'
                   '第四個參數為垂直延伸格數，此處為 1，第五個參數為水平延伸格'
                   '數，此處為 7')

    print('INFO')
    MyNotifyDialog.info(longMessage)
    print('WARN')
    MyNotifyDialog.warn(longMessage)
    print('ERROR')
    MyNotifyDialog.error(longMessage)
    print('CONFIRM')
    ret = MyNotifyDialog.confirm(longMessage)
    print(ret)
    ret = MyNotifyDialog.confirm(longMessage)
    print(ret)
