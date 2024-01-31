n = int(input("▪ Enter  number:"))

def pascal(n):
    for line in range (0, n):
        for i in range (0, line+1):
            print(fun_1(line, i), " " , end="")
        print()

def fun_1(n, k):
    result=1
    if(k>n-k):
        k=n-k
    for i in range(0, k):
        result= result*(n-i)
        result=result//(i+1)
    return result

pascal(n)