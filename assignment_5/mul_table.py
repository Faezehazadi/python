n = int(input("▪ Enter  row:"))
m = int(input("▪ Enter column:"))

def mul_table(n, m):
    for i in range(1, n+1):
        for j in range (1, m+1):
            mul=i*j
            print (mul, end =" ")
        print()

mul_table(n,m)       