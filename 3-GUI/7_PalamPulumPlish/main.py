
import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_Palam_Pulum_Plish import Ui_MainWindow

class Mainwindow ( QMainWindow ):

    def __init__ ( self ) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

        self.ui.back.setText ("🤚🏻")
        self.ui.front.setText ("✋🏻")
        self.c1_score = 0
        self.c2_score = 0
        self.player_score = 0

        self.ui.front.clicked.connect (partial (self.play , "front"))
        self.ui.back.clicked.connect (partial (self.play , "back"))

    def play ( self , player ) :
        self.ui.player.setText ("")
        self.ui.computer1.setText ("")
        self.ui.computer2.setText ("")
        self.c1 = random.randint (0 , 1)
        self.c2 = random.randint (0 , 1)
        self.player_mode = player

        if self.player_mode == "front" :
            self.ui.player.setText ("✋")
        
        else :
            self.ui.player.setText ("🤚")


        if self.c1 == 0 :
            self.ui.computer1.setText ("✋")
            self.c1_mode = "front"
        
        else :
            self.ui.computer1.setText ("🤚")
            self.c1_mode = "back"

        
        if self.c2 == 0 :
            self.ui.computer2.setText ("✋")
            self.c2_mode = "front"
        
        else :
            self.ui.computer2.setText ("🤚")
            self.c2_mode = "back"

        self.check_win ()
        text = ""

        if self.player_score == 5 :
            text = f" 🎈 Player wins  🎈"
        
        elif self.c1_score == 5 :
            text = f"🎈 Computer1 wins  🎈"
        
        elif self.c2_score == 5 :
            text = "🎈 Computer2 wins  🎈"
        
        if text != "" :
            self.player_score = 0
            self.c1_score = 0
            self.c2_score = 0
            self.ui.player.setText ("")
            self.ui.computer1.setText ("")
            self.ui.computer2.setText ("")
            self.ui.player_score.setText (str (self.player_score))
            self.ui.scoreC1.setText (str (self.c1_score))
            self.ui.scoreC2.setText (str (self.c2_score))
            message = QMessageBox (windowTitle = "congratulation" , text = text)
            message.exec_ ()

    def check_win ( self ) :
        if self.player_mode == self.c1_mode == self.c2_mode :
            self.ui.win.setText ("equal")

        elif self.player_mode == self.c1_mode != self.c2_mode :
            self.ui.win.setText ("Computer2 Wins")
            self.c2_score += 1
            self.ui.scoreC2.setText (str (self.c2_score))

        elif self.player_mode == self.c2_mode != self.c1_mode :
            self.ui.win.setText ("Computer1 Wins")
            self.c1_score += 1
            self.ui.scoreC1.setText (str (self.c1_score))

        elif self.c1_mode == self.c2_mode != self.player_mode :
            self.ui.win.setText ("Player Wins")
            self.player_score += 1
            self.ui.player_score.setText (str (self.player_score))

app = QApplication ( sys.argv )
window = Mainwindow ()
window.show ()
app.exec ()