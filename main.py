import requests
import json
import sys
from mwin import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTranslator, QUrl, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QDesktopServices, QPixmap

query_string = ''
headers = {'User-Agent': 'Mozilla/5.0'}


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_opponent.released.connect(self.get_opponent)
        self.pushButton_match.released.connect(self.get_match)

    def get_opponent(self):
        query_string = self.textEdit_name.toPlainText()
        url_opponent = f'https://aoe2.net/api/nightbot/opponent?search={query_string}'
        response = requests.get(url_opponent, headers=headers)
        toprint = response.content.decode('utf-8')
        self.textBrowser.clear()
        self.textBrowser.append(toprint)

    def get_match(self):
        query_string = self.textEdit_name.toPlainText()
        url_match = f'https://aoe2.net/api/nightbot/match?search={query_string}'
        response = requests.get(url_match, headers=headers)
        toprint = response.content.decode('utf-8')
        self.textBrowser.clear()
        self.textBrowser.append(toprint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
