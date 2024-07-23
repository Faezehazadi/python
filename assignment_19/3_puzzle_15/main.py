
import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui_puzzle_15 import Ui_MainWindow

class MainWindow ( QMainWindow ) :
    def __init__ (self , num_list) :
        super().__init__()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi ( self )
        self.buttons = [[ self.ui.one , self.ui.two , self.ui.three , self.ui.four ] ,
                        [ self.ui.five , self.ui.six , self.ui.seven , self.ui.eight ] ,
                        [self.ui.nine , self.ui.ten , self.ui.eleven , self.ui.tewelve ] ,
                        [ self.ui.thirteen , self.ui.fourteen , self.ui.fifteen , self.ui.sixteen ]]
        
        for i in range (4) :
            for j in range (4) :
                self.buttons[i][j].setText ( str(num_list[i][j]) )
                self.buttons[i][j].clicked.connect (partial (self.play , i , j))
                if num_list[i][j] == 16 :
                    self.buttons[i][j].setVisible (False)
                    self.empty_i = i
                    self.empty_j = j
        

    def play (self , i , j) :
        if (i == self.empty_i and abs (j - self.empty_j) == 1) or (j == self.empty_j and abs (i - self.empty_i) == 1) :
            self.buttons[self.empty_i][self.empty_j].setText (self.buttons[i][j].text())
            self.buttons[i][j].setText ("16")
            self.buttons[i][j].setVisible (False)
            self.buttons[self.empty_i][self.empty_j].setVisible (True)
            self.empty_i = i
            self.empty_j = j

        if self.win () == True :
            message = QMessageBox ( text = " YOU WIN 🎈 ")
            message.exec_()

    def win (self) :
        index = 1
        for i in range (4) :
            for j in range (4) :
                if int (self.buttons[i][j].text()) != index :
                    return False
                
                else :
                    index += 1

        return True

       
number_list = []
used_number = []
for i in range (4) :
    number = []
    while len(number) < 4 :
        x = random.randint ( 1 , 16 )
        if x not in used_number :
            number.append (x)
            used_number.append (x)
    
    number_list.append (number)

app = QApplication ( sys.argv )
window = MainWindow ( number_list )
window.show ()
app.exec ()