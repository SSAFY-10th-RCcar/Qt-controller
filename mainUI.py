# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_w = QPushButton(self.centralwidget)
        self.btn_w.setObjectName(u"btn_w")
        self.btn_w.setGeometry(QRect(190, 320, 71, 61))
        self.btn_w.setMouseTracking(False)
        self.btn_d = QPushButton(self.centralwidget)
        self.btn_d.setObjectName(u"btn_d")
        self.btn_d.setGeometry(QRect(270, 390, 71, 61))
        self.btn_d.setMouseTracking(False)
        self.btn_s = QPushButton(self.centralwidget)
        self.btn_s.setObjectName(u"btn_s")
        self.btn_s.setGeometry(QRect(190, 390, 71, 61))
        self.btn_s.setMouseTracking(False)
        self.btn_a = QPushButton(self.centralwidget)
        self.btn_a.setObjectName(u"btn_a")
        self.btn_a.setGeometry(QRect(110, 390, 71, 61))
        self.btn_a.setMouseTracking(False)
        self.logText = QLabel(self.centralwidget)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(20, 40, 341, 211))
        self.logText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.sensingText = QLabel(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(420, 40, 341, 211))
        self.sensingText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_w.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.btn_d.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.btn_s.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.btn_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.logText.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.sensingText.setText(QCoreApplication.translate("MainWindow", u"sense", None))
    # retranslateUi

