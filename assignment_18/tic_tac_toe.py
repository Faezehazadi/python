import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def about():
    msg_box = QMessageBox(windowTitle="about Tic-tac-toe game", text="TicTacToe is an exciting two player game. If you align 3 pieces in a row you will win the game.")
    msg_box.exec()

#clear the button's text 
def clear():
    for i in range(3):
        for j in range(3):
            btns[i][j].setText("")

def new_game():
    global x_score
    global o_score
    global ties
    x_score = o_score = ties = 0
    main_window.btn_x_score.setText("X: " + str(x_score))
    main_window.btn_o_score.setText("O: " + str(o_score))
    main_window.btn_ties.setText("T: " + str(ties))
    clear()   

def check():
    global x_score
    global o_score
    # to count the number of draw in the game
    global ties
    global state
    state = "false"
    for i in range(3):
        if btns[i][0].text() == "X" and btns[i][1].text() == "X" and btns[i][2].text() == "X" or btns[0][i].text() == "X" and btns[1][i].text() == "X" and btns[2][i].text() == "X" or btns[0][0].text() == "X" and btns[1][1].text() == "X" and btns[2][2].text() == "X" or btns[0][2].text() == "X" and btns[1][1].text() == "X" and btns[2][0].text() == "X":
            msg_box = QMessageBox(text=" 🎈 Player 1 wins")
            msg_box.exec()
            x_score += 1
            #show the score of player 1 after new update
            main_window.btn_x_score.setText("X:" + str(x_score))
            clear()
            state = "true"
        elif btns[i][0].text() == "O" and btns[i][1].text() == "O" and btns[i][2].text() == "O" or btns[0][i].text() == "O" and btns[1][i].text() == "O" and btns[2][i].text() == "O" or btns[0][0].text() == "O" and btns[1][1].text() == "O" and btns[2][2].text() == "O" or btns[0][2].text() == "O" and btns[1][1].text() == "O" and btns[2][0].text() == "O":
            msg_box = QMessageBox(text=" 🎈 Player 2 wins")
            msg_box.exec()
            o_score += 1
            main_window.btn_o_score.setText("O:" + str(o_score))
            clear()
            state = "true"
            # if all the buttons are filled and neither player has won, then the result of the game is draw
        elif btns[0][0].text() != "" and btns[1][0].text() != "" and btns[2][0].text() != "" and btns[0][1].text() != "" and btns[1][1].text() != "" and btns[2][1].text() != "" and btns[0][2].text() != "" and btns[1][2].text() != "" and btns[2][2].text() != "":
            msg_box = QMessageBox(text="darw")
            msg_box.exec()
            ties += 1
            main_window.btn_ties.setText("Ties: " + str(ties))
            clear()
            state = "true"

def mode(a):
    global mode
    mode = a

def play(row, col):
    global player
    global state

    if mode == "player1_player2":
        if player == 1 and btns[row][col].text() == "":
            btns[row][col].setText("X")
            btns[row][col].setStyleSheet("color:darkpink;")
            player = 2
        elif player == 2 and btns[row][col].text() == "":
            btns[row][col].setText("O")
            btns[row][col].setStyleSheet("color:white;")
            player = 1

    elif mode == "player_cpu":
        if player == 1 and btns[row][col].text() == "":
            btns[row][col].setText("X")
            btns[row][col].setStyleSheet("color:darkpink;")
            check()

            if state == "false":
                while True:
                    row_cpu = random.randint(0, 2)
                    col_cpu = random.randint(0, 2)
                    if btns[row_cpu][col_cpu].text() == "" and row_cpu != row and col_cpu != col:
                        btns[row_cpu][col_cpu].setText("O")
                        btns[row_cpu][col_cpu].setStyleSheet("color:white;")
                        break

    check()

loader = QUiLoader()
app = QApplication(sys.argv)
player = 1
main_window = loader.load("tic_tac_toe.ui")
main_window.show()

btns = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
        [main_window.btn_4, main_window.btn_5, main_window.btn_6],
        [main_window.btn_7, main_window.btn_8, main_window.btn_9],]

new_game()

for i in range(3):
    for j in range(3):
        btns[i][j].clicked.connect(partial(play, i, j))

main_window.btn_new_game.clicked.connect(new_game)
main_window.btn_about.clicked.connect(about)
main_window.rbtn_player_vs_player.pressed.connect(partial(mode, "player1_player2"))
main_window.rbtn_player_vs_cpu.pressed.connect(partial(mode, "player_cpu"))

app.exec()

#state?