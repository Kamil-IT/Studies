# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(403, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setGeometry(QRect(300, 74, 93, 49))
        font = QFont()
        font.setPointSize(20)
        self.pushButton_minus.setFont(font)
        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(300, 134, 93, 49))
        self.pushButton_plus.setFont(font)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 74, 279, 49))
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_1 = QPushButton(self.splitter)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setFont(font)
        self.splitter.addWidget(self.pushButton_1)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.splitter.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.splitter.addWidget(self.pushButton_3)
        self.pushButton_star = QPushButton(self.centralwidget)
        self.pushButton_star.setObjectName(u"pushButton_star")
        self.pushButton_star.setGeometry(QRect(300, 194, 93, 49))
        self.pushButton_star.setFont(font)
        self.pushButton_bravely = QPushButton(self.centralwidget)
        self.pushButton_bravely.setObjectName(u"pushButton_bravely")
        self.pushButton_bravely.setGeometry(QRect(300, 250, 93, 49))
        self.pushButton_bravely.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 0, 381, 61))
        font1 = QFont()
        font1.setPointSize(22)
        self.textEdit.setFont(font1)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 134, 279, 49))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_5 = QSplitter(self.splitter_2)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.pushButton_4 = QPushButton(self.splitter_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.splitter_5.addWidget(self.pushButton_4)
        self.pushButton_5 = QPushButton(self.splitter_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        self.splitter_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.splitter_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)
        self.splitter_5.addWidget(self.pushButton_6)
        self.splitter_2.addWidget(self.splitter_5)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(10, 194, 279, 49))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_4 = QSplitter(self.splitter_3)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.pushButton_7 = QPushButton(self.splitter_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)
        self.splitter_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QPushButton(self.splitter_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font)
        self.splitter_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QPushButton(self.splitter_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font)
        self.splitter_4.addWidget(self.pushButton_9)
        self.splitter_3.addWidget(self.splitter_4)
        self.splitter_6 = QSplitter(self.centralwidget)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(105, 250, 185, 49))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.pushButton_equal = QPushButton(self.splitter_6)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setFont(font)
        self.splitter_6.addWidget(self.pushButton_equal)
        self.pushButton_C = QPushButton(self.centralwidget)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setGeometry(QRect(10, 250, 91, 49))
        self.pushButton_C.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 403, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_star.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_bravely.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi
