import random
from functools import partial
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_guess import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_check.clicked.connect(self.check)
        self.computer_number = random.randint(0, 100)
        self.counter = 0


    def check(self):
        for i in range(7):
            if int(self.ui.lineEdit.text()) < self.computer_number:
               self.ui.lineEdit_2.setText("go up")
               self.ui.lineEdit.setText("")
               self.counter += 1
               self.ui.lineEdit_3.setText(str(self.counter))
               if self.counter == 6:
                   self.ui.lineEdit_2.setText("you failed")

            elif int(self.ui.lineEdit.text()) > self.computer_number:
                 self.ui.lineEdit_2.setText("go down")
                 self.ui.lineEdit.setText("")
                 self.counter += 1
                 self.ui.lineEdit_3.setText(str(self.counter))
                 if self.counter == 6:
                     self.ui.lineEdit_2.setText("you failed")

            elif int(self.ui.lineEdit.text()) == self.compuetr_number:
                 self.ui.lineEdit_2.setText("you win")
                 self.counter +=1
                 self.ui.lineEdit_3.setText(str(self.counter))
                 msg_box = QMessageBox()
                 msg_box.setText("do you want to play again?")
                 msg_box.exec()
                 self.reset()

        if self.ui.lineEdit_2.text() == "you failed":
            msg_box = QMessageBox()
            msg_box.setText("the correct answer was:" + str(self.computer_number) + "play again?")
            msg_box.exec()
            self.reset()

    def reset(self):
        self.computer_number = random.randint(0, 100)
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit.setText("")
        self.counter = 0



app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()


app.exec()