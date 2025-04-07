# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rps.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 427)
        MainWindow.setStyleSheet(u"background-color: rgb(169, 188, 105);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.show_computer = QLabel(self.centralwidget)
        self.show_computer.setObjectName(u"show_computer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_computer.sizePolicy().hasHeightForWidth())
        self.show_computer.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(18)
        font.setBold(True)
        font.setKerning(True)
        self.show_computer.setFont(font)
        self.show_computer.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.show_computer.setStyleSheet(u"background-color: rgb(67, 58, 54);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.show_computer, 1, 0, 1, 2)

        self.show_player = QLabel(self.centralwidget)
        self.show_player.setObjectName(u"show_player")
        sizePolicy.setHeightForWidth(self.show_player.sizePolicy().hasHeightForWidth())
        self.show_player.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.show_player.setFont(font1)
        self.show_player.setStyleSheet(u"background-color: rgb(67, 58, 54);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.show_player, 1, 2, 1, 2)

        self.computer_score = QLabel(self.centralwidget)
        self.computer_score.setObjectName(u"computer_score")
        sizePolicy.setHeightForWidth(self.computer_score.sizePolicy().hasHeightForWidth())
        self.computer_score.setSizePolicy(sizePolicy)
        self.computer_score.setFont(font1)
        self.computer_score.setStyleSheet(u"background-color: rgb(255, 147, 38);")

        self.gridLayout.addWidget(self.computer_score, 2, 0, 1, 2)

        self.player_score = QLabel(self.centralwidget)
        self.player_score.setObjectName(u"player_score")
        sizePolicy.setHeightForWidth(self.player_score.sizePolicy().hasHeightForWidth())
        self.player_score.setSizePolicy(sizePolicy)
        self.player_score.setFont(font1)
        self.player_score.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.player_score.setStyleSheet(u"background-color: rgb(255, 147, 38);")

        self.gridLayout.addWidget(self.player_score, 2, 2, 1, 2)

        self.win = QLabel(self.centralwidget)
        self.win.setObjectName(u"win")
        sizePolicy.setHeightForWidth(self.win.sizePolicy().hasHeightForWidth())
        self.win.setSizePolicy(sizePolicy)
        self.win.setFont(font1)
        self.win.setStyleSheet(u"background-color: rgb(67, 58, 54);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.win, 3, 0, 1, 4)

        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_rock.sizePolicy().hasHeightForWidth())
        self.btn_rock.setSizePolicy(sizePolicy1)
        self.btn_rock.setFont(font1)
        self.btn_rock.setStyleSheet(u"background-color: rgb(255, 51, 150);")

        self.gridLayout.addWidget(self.btn_rock, 4, 0, 1, 1)

        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        sizePolicy1.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy1)
        self.btn_paper.setFont(font1)
        self.btn_paper.setStyleSheet(u"background-color: rgb(255, 51, 150);")

        self.gridLayout.addWidget(self.btn_paper, 4, 1, 1, 2)

        self.btn_scissor = QPushButton(self.centralwidget)
        self.btn_scissor.setObjectName(u"btn_scissor")
        sizePolicy1.setHeightForWidth(self.btn_scissor.sizePolicy().hasHeightForWidth())
        self.btn_scissor.setSizePolicy(sizePolicy1)
        self.btn_scissor.setFont(font1)
        self.btn_scissor.setStyleSheet(u"background-color: rgb(255, 51, 150);")

        self.gridLayout.addWidget(self.btn_scissor, 4, 3, 1, 1)

        self.label_player = QLabel(self.centralwidget)
        self.label_player.setObjectName(u"label_player")
        sizePolicy.setHeightForWidth(self.label_player.sizePolicy().hasHeightForWidth())
        self.label_player.setSizePolicy(sizePolicy)
        self.label_player.setFont(font1)
        self.label_player.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.label_player, 0, 2, 1, 2)

        self.label_computer = QLabel(self.centralwidget)
        self.label_computer.setObjectName(u"label_computer")
        sizePolicy.setHeightForWidth(self.label_computer.sizePolicy().hasHeightForWidth())
        self.label_computer.setSizePolicy(sizePolicy)
        self.label_computer.setFont(font1)
        self.label_computer.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.label_computer, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 501, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.show_computer.setText("")
        self.show_player.setText("")
        self.computer_score.setText(QCoreApplication.translate("MainWindow", u"   Computer : 0", None))
        self.player_score.setText(QCoreApplication.translate("MainWindow", u"      You = 0", None))
        self.win.setText("")
        self.btn_rock.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.btn_paper.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.btn_scissor.setText(QCoreApplication.translate("MainWindow", u"scissor", None))
        self.label_player.setText(QCoreApplication.translate("MainWindow", u"          You", None))
        self.label_computer.setText(QCoreApplication.translate("MainWindow", u"       Computer", None))
    # retranslateUi

