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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_w = QPushButton(self.centralwidget)
        self.btn_w.setObjectName(u"btn_w")
        self.btn_w.setGeometry(QRect(160, 340, 71, 71))
        self.btn_d = QPushButton(self.centralwidget)
        self.btn_d.setObjectName(u"btn_d")
        self.btn_d.setGeometry(QRect(250, 420, 71, 71))
        self.btn_s = QPushButton(self.centralwidget)
        self.btn_s.setObjectName(u"btn_s")
        self.btn_s.setGeometry(QRect(160, 420, 71, 71))
        self.btn_a = QPushButton(self.centralwidget)
        self.btn_a.setObjectName(u"btn_a")
        self.btn_a.setGeometry(QRect(70, 420, 71, 71))
        self.btn_leftforward = QPushButton(self.centralwidget)
        self.btn_leftforward.setObjectName(u"btn_leftforward")
        self.btn_leftforward.setGeometry(QRect(470, 310, 71, 71))
        self.btn_leftbackward = QPushButton(self.centralwidget)
        self.btn_leftbackward.setObjectName(u"btn_leftbackward")
        self.btn_leftbackward.setGeometry(QRect(470, 470, 71, 71))
        self.btn_rightforward = QPushButton(self.centralwidget)
        self.btn_rightforward.setObjectName(u"btn_rightforward")
        self.btn_rightforward.setGeometry(QRect(650, 310, 71, 71))
        self.btn_forward = QPushButton(self.centralwidget)
        self.btn_forward.setObjectName(u"btn_forward")
        self.btn_forward.setGeometry(QRect(560, 310, 71, 71))
        self.btn_rightbackward = QPushButton(self.centralwidget)
        self.btn_rightbackward.setObjectName(u"btn_rightbackward")
        self.btn_rightbackward.setGeometry(QRect(650, 470, 71, 71))
        self.btn_backward = QPushButton(self.centralwidget)
        self.btn_backward.setObjectName(u"btn_backward")
        self.btn_backward.setGeometry(QRect(560, 470, 71, 71))
        self.sensingText = QLabel(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setGeometry(QRect(70, 30, 651, 271))
        self.sensingText.setFrameShape(QFrame.Panel)
        self.sensingText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(560, 390, 71, 71))
        self.record_num = QLabel(self.centralwidget)
        self.record_num.setObjectName(u"record_num")
        self.record_num.setGeometry(QRect(70, 0, 121, 31))
        self.record_num.setFrameShape(QFrame.Panel)
        self.record_num.setAlignment(Qt.AlignCenter)
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
        self.btn_leftforward.setText(QCoreApplication.translate("MainWindow", u"\u2196", None))
        self.btn_leftbackward.setText(QCoreApplication.translate("MainWindow", u"\u2199", None))
        self.btn_rightforward.setText(QCoreApplication.translate("MainWindow", u"\u2197", None))
        self.btn_forward.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.btn_rightbackward.setText(QCoreApplication.translate("MainWindow", u"\u2198", None))
        self.btn_backward.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.sensingText.setText("")
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.record_num.setText("")
    # retranslateUi

