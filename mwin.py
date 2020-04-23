# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\rating-peeker.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 270)
        MainWindow.setMinimumSize(QtCore.QSize(495, 270))
        MainWindow.setMaximumSize(QtCore.QSize(495, 270))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mwin/icons/aoe2_de.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_name.setGeometry(QtCore.QRect(20, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.textEdit_name.setFont(font)
        self.textEdit_name.setObjectName("textEdit_name")
        self.pushButton_opponent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_opponent.setGeometry(QtCore.QRect(270, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.pushButton_opponent.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/1v1/icons/difficulty_easy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_opponent.setIcon(icon1)
        self.pushButton_opponent.setObjectName("pushButton_opponent")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 451, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setLineWidth(2)
        self.textBrowser.setMidLineWidth(2)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_match = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_match.setGeometry(QtCore.QRect(270, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.pushButton_match.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tg/icons/difficulty_medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_match.setIcon(icon2)
        self.pushButton_match.setObjectName("pushButton_match")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShortcutGUI for aoe2.net"))
        self.textEdit_name.setPlaceholderText(_translate("MainWindow", "Type your in game name here"))
        self.pushButton_opponent.setText(_translate("MainWindow", "Opponent (1v1)"))
        self.pushButton_match.setText(_translate("MainWindow", "Match Info"))
        
import source_rc
