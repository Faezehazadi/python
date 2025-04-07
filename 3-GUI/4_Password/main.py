import random
import sys
import string
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_password_generator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.password_length = 0
        self.word_list = list (string.ascii_letters + string.digits + string.punctuation)

        self.ui.radioB_normal.clicked.connect(self.password_mode)
        self.ui.radioB_hard.clicked.connect(self.password_mode)
        self.ui.radioB_extrahard.clicked.connect(self.password_mode)
        self.ui.btn_generate.clicked.connect(self.show_password)

    def password_mode(self):
        if self.ui.radioB_normal.isChecked():
            self.password_length = 6
            self.password = "".join(random.sample(self.word_list, self.password_length))

        elif self.ui.radioB_hard.isChecked():
            self.password_length = 8
            self.password = "".join(random.sample(self.word_list, self.password_length))

        elif self.ui.radioB_extrahard.isChecked():
            self.password_length = 12
            self.password = "".join(random.sample(self.word_list, self.password_length))
    
    def show_password(self):
        self.ui.textbox_password.setText("")
        self.ui.textbox_password.setText(self.password)
    
if __name__ =="__main__":
    app = QApplication(sys.argv)
    

    mainwindow = MainWindow()
    mainwindow.show()


    app.exec()



            