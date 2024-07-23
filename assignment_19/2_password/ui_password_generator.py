# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(313, 331)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textbox_password = QLineEdit(self.centralwidget)
        self.textbox_password.setObjectName(u"textbox_password")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(11)
        self.textbox_password.setFont(font)
        self.textbox_password.setStyleSheet(u"background-color: rgb(149, 218, 60);")

        self.gridLayout.addWidget(self.textbox_password, 0, 0, 1, 1)

        self.radioB_normal = QRadioButton(self.centralwidget)
        self.radioB_normal.setObjectName(u"radioB_normal")
        self.radioB_normal.setFont(font)

        self.gridLayout.addWidget(self.radioB_normal, 1, 0, 1, 1)

        self.radioB_hard = QRadioButton(self.centralwidget)
        self.radioB_hard.setObjectName(u"radioB_hard")
        self.radioB_hard.setFont(font)

        self.gridLayout.addWidget(self.radioB_hard, 2, 0, 1, 1)

        self.radioB_extrahard = QRadioButton(self.centralwidget)
        self.radioB_extrahard.setObjectName(u"radioB_extrahard")
        self.radioB_extrahard.setFont(font)

        self.gridLayout.addWidget(self.radioB_extrahard, 3, 0, 1, 1)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet(u"background-color: rgb(209, 255, 165);")

        self.gridLayout.addWidget(self.btn_generate, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 313, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioB_normal.setText(QCoreApplication.translate("MainWindow", u"generate  a normal strength password\n"
"(6 characters)", None))
        self.radioB_hard.setText(QCoreApplication.translate("MainWindow", u"generate hard strength password\n"
"(including 8 )", None))
        self.radioB_extrahard.setText(QCoreApplication.translate("MainWindow", u"generate extra hard strength password\n"
"(12 characters)", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u" Generate Password", None))
    # retranslateUi

