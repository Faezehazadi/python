num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

if num1 != 0 and num2 != 0:
    if (num1)>(num2):
        n=(num2)
    else:
        n=(num1)

    for i in range(n,0,-1):
        if (num1)%i== 0 and (num2)%i== 0:
            Bmm=i
            break
else:
   Bmm=0     

print("Greatest common divisor: ",Bmm)   