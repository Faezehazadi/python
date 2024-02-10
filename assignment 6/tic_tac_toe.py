from termcolor import colored
import random
import time

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print( )


def check_game_a(game_board):
        if game_board[1][0] == game_board[1][1] == game_board[1][2] == (colored("X", "red")) or game_board[2][0] == game_board[2][1] == game_board[2][2] == (colored("X", "red")) or game_board[0][0] == game_board[1][0] == game_board[2][0] == (colored("X", "red")) or game_board[0][1] == game_board[1][1] == game_board[2][1] == (colored("X", "red")) or game_board[0][2] == game_board[1][2] == game_board[2][2] == (colored("X", "red")) or game_board[0][0] == game_board[1][1] == game_board[2][2] == (colored("X", "red")) or game_board[0][2] == game_board[1][1] == game_board[2][0] == (colored("X", "red")) or game_board[0][0] == game_board[0][1] == game_board[0][2] == (colored("X", "red")):
            print("🎈player_1🎈")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)
        elif  game_board[1][0] == game_board[1][1] == game_board[1][2] == (colored("O", "blue")) or game_board[0][0] == game_board[0][1] == game_board[0][2] == (colored("O", "blue")) or game_board[2][0] == game_board[2][1] == game_board[2][2] == (colored("O", "blue")) or game_board[0][0] == game_board[1][0] == game_board[2][0] == (colored("O", "blue")) or game_board[0][1] == game_board[1][1] == game_board[2][1] == (colored("O", "blue")) or game_board[0][2] == game_board[1][2] == game_board[2][2] == (colored("O", "blue")) or game_board[0][0] == game_board[1][1] == game_board[2][2] == (colored("O", "blue")) or game_board[0][2] == game_board[1][1] == game_board[2][0] == (colored("O", "blue")):
            print("🎈player_2🎈")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)
        elif game_board[0][0]!= "_" and game_board[0][1]!= "_" and game_board[0][2]!= "_" and game_board[1][0]!= "_" and game_board[1][1]!= "_" and game_board[1][2]!= "_" and game_board[2][0]!= "_" and game_board[2][1]!= "_" and game_board[2][2] != "_":
            print("0-0")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)

def check_game_b(game_board):
        if game_board[1][0] == game_board[1][1] == game_board[1][2] == (colored("X", "red")) or game_board[2][0] == game_board[2][1] == game_board[2][2] == (colored("X", "red")) or game_board[0][0] == game_board[1][0] == game_board[2][0] == (colored("X", "red")) or game_board[0][1] == game_board[1][1] == game_board[2][1] == (colored("X", "red")) or game_board[0][2] == game_board[1][2] == game_board[2][2] == (colored("X", "red")) or game_board[0][0] == game_board[1][1] == game_board[2][2] == (colored("X", "red")) or game_board[0][2] == game_board[1][1] == game_board[2][0] == (colored("X", "red")) or game_board[0][0] == game_board[0][1] == game_board[0][2] == (colored("X", "red")):
            print("🎈player_1🎈")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)
        elif game_board[0][0] == game_board[0][1] == game_board[0][2] == (colored("O", "blue")) or game_board[1][0] == game_board[1][1] == game_board[1][2] == (colored("O", "blue")) or game_board[2][0] == game_board[2][1] == game_board[2][2] == (colored("O", "blue")) or game_board[0][0] == game_board[1][0] == game_board[2][0] == (colored("O", "blue")) or game_board[0][1] == game_board[1][1] == game_board[2][1] == (colored("O", "blue")) or game_board[0][2] == game_board[1][2] == game_board[2][2] == (colored("O", "blue")) or game_board[0][0] == game_board[1][1] == game_board[2][2] == (colored("O", "blue")) or game_board[0][2] == game_board[1][1] == game_board[2][0] == (colored("O", "blue")):
            print("🎈pc🎈")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)
        elif game_board[0][0]!= "_" and game_board[0][1]!= "_" and game_board[0][2]!= "_" and game_board[1][0]!= "_" and game_board[1][1]!= "_" and game_board[1][2]!= "_" and game_board[2][0]!= "_" and game_board[2][1]!= "_" and game_board[2][2] != "_":
            print("0-0")
            end = time.time()
            d=int(end-start)
            print("Time:", d )
            exit(0)

def main_menu():
    print ("1️⃣  👩 💻")
    print ("2️⃣  👩 🧑 ") 
    
while True:
    main_menu()
    game_board = [["_", "_", "_"],
                 ["_", "_", "_"],
                 ["_", "_", "_"]]

    show()
    ch = int(input("◾Enter your choice between  1️⃣  , 2️⃣  : "))
    start = time.time()

    if ch == 1:
        while True:
            print("👩 Player1: ")

            while True :
                row = int(input("◾ enter row: "))
                col = int (input("◾ enter column: "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("choose another numbers.")
                else :
                    print ("choose between 0 , 1 , 2.")

            show()
            check_game_a(game_board)

            print("🧑 Player2: ")
            while True :
                row = int(input("◾ enter row: "))
                col = int (input("◾ enter column : "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("O", "blue"))
                        break
                    else :
                        print("choose another numbers.")
                else :
                    print ("choose between 0 , 1 , 2.")
            show()
            check_game_a(game_board)


    elif ch  == 2:
        show()
        while True:
            print("👩 you:")

            while True :
                row=int(input("◾ enter row : "))
                col=int (input("◾ enter column : "))
                if 0<=row<=2 and 0<=col<=2 :
                    if game_board[row][col] == "_":
                        game_board[row][col] = (colored("X", "red"))
                        break
                    else :
                     print("choose another numbers.")
                else :
                    print ("choose between 0 , 1 , 2.")

            show()
            check_game_b(game_board)

            print("💻 PC:")
            while True :
                raw=random.randint(0, 2)
                col=random.randint(0, 2)
                if game_board[col][row] == "_":
                    game_board[col][row] = (colored("O", "blue"))
                    break
                else:
                    continue
            show()
            check_game_b(game_board)
