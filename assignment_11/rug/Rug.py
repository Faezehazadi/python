n = int(input("Enter number: "))

def Generate_Rug(n):
    if n % 2 != 0:
        pattern = ["🧁", "🍧", "🍭", "🍷", "🍦", "🍬", "🍥", "🎂"]
        rug = [[0] * n for i in range(n)]
        middle = n // 2
        
        for i in range(middle, -1, -1):
            for j in range(n):
                rug[i][j] = pattern[middle - i]
                rug[n-1-i][j] = pattern[middle - i]
                rug[j][i] = pattern[middle - i]
                rug[j][n-1-i] = pattern[middle - i]
                
        for row in rug:
            for c in row:
                print(c, end=' ')
            print()
        
    elif n<=0 :
        print("🔸 enter another number. ")

    else:
        print("🔸 enter odd number. ")    
                
Generate_Rug(n)