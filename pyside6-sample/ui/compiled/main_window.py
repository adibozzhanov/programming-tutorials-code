# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QScrollBar, QSizePolicy, QStatusBar, QWidget)

class Ui_thing(object):
    def setupUi(self, thing):
        if not thing.objectName():
            thing.setObjectName(u"thing")
        thing.resize(800, 600)
        self.centralwidget = QWidget(thing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.COOLBUTTON = QPushButton(self.centralwidget)
        self.COOLBUTTON.setObjectName(u"COOLBUTTON")
        self.COOLBUTTON.setGeometry(QRect(520, 140, 103, 36))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(350, 310, 113, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(290, 180, 113, 36))
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(640, 250, 16, 160))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(40, 100, 50, 64))
        thing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(thing)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuForm = QMenu(self.menubar)
        self.menuForm.setObjectName(u"menuForm")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        thing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(thing)
        self.statusbar.setObjectName(u"statusbar")
        thing.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(thing)

        QMetaObject.connectSlotsByName(thing)
    # setupUi

    def retranslateUi(self, thing):
        thing.setWindowTitle(QCoreApplication.translate("thing", u"MainWindow", None))
        self.COOLBUTTON.setText(QCoreApplication.translate("thing", u"OK", None))
        self.radioButton.setText(QCoreApplication.translate("thing", u"RadioButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("thing", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("thing", u"Edit", None))
        self.menuForm.setTitle(QCoreApplication.translate("thing", u"Form", None))
        self.menuView.setTitle(QCoreApplication.translate("thing", u"View", None))
    # retranslateUi

