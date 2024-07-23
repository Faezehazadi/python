import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow
from ui_rps import Ui_MainWindow


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.computer_score=0
        self.player_score=0
        self.ui.btn_paper.clicked.connect(partial(self.Paper))
        self.ui.btn_rock.clicked.connect(partial(self.Rock))
        self.ui.btn_scissor.clicked.connect(partial(self.Scissor))

    def Rock(self):
        self.computer=random.choice(["Rock", "Paper", "Scissor"])
        self.ui.show_player.setText("Rock")
        self.ui.show_computer.setText(self.computer)
        self.check() 

    def Paper(self):
        self.computer=random.choice(["Rock", "Paper", "Scissor"])
        self.ui.show_player.setText("Paper")
        self.ui.show_computer.setText(self.computer) 
        self.check()

    def Scissor(self):
        self.computer=random.choice(["Rock", "Paper", "Scissor"])
        self.ui.show_player.setText("Scissor")
        self.ui.show_computer.setText(self.computer) 
        self.check()

    def check(self):
        if self.computer == "Rock" and self.ui.show_player.text()=="Paper":
            self.player_score+=1
            self.ui.win.setText(" win 🎈 ")
        elif self.computer == "Rock" and self.ui.show_player.text()=="Scissor":
            self.computer_score+=1
            self.ui.win.setText(" fail 💔 ")
        elif self.computer == "Paper" and self.ui.show_player.text()=="Rock":
            self.computer_score+=1
            self.ui.win.setText(" fail 💔 ")
        elif self.computer == "Paper" and self.ui.show_player.text()=="Scissor":
            self.player_score+=1
            self.ui.win.setText(" win 🎈 ")
        elif self.computer == "Scissor" and self.ui.show_player.text()=="Rock":
            self.player_score+=1
            self.ui.win.setText(" win 🎈 ")
        elif self.computer == "Scissor" and self.ui.show_player.text()=="Paper":
            self.computer_score+=1
            self.ui.win.setText(" fail 💔 ")
        elif self.computer ==  self.ui.show_player.text():
            self.ui.win.setText(" equal 😁 ")

        self.ui.player_score.setText(f"Player_score:{str(self.player_score)}")
        self.ui.computer_score.setText(f"computer_score:{str(self.computer_score)}")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=Main_Window()
    main_window.show()

    app.exec()