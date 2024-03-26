n = int(input("▪ Enter  row:"))
m = int(input("▪ Enter column:"))

def chessboard(n, m):
    for i in range(n):
        for j in range (m):
            if(i+j) % 2 ==0:
                print("🌝", end =" ")
            else:
                print("🌑", end =" ")
        print()
        
chessboard(n, m)