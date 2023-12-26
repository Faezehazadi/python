import math

print("Choose your operation:")
print("1)sum")
print("2)sub")
print("3)mul")
print("4)div")
print("5)sin")
print("6)cos")
print("7)tan")
print("8)cot")
print("9)factorial")
print("10)sqrt")


op = int(input("enter your choice:"))


if op==1 or op==2 or op==3 or op==4:
    a = float(input("Enter num1:"))
    b = float(input("Enter num2:"))

else:
   a = int(input("enter num:")) 

if op == 1:
    c = a+b

elif op == 2:
    c = a-b

elif op == 3:
    c = a*b

elif op == 4:
    if b == 0:
        c = print("false")
    else:    
         c = a/b

elif op == 5:
    d = (a*math.pi)/180
    c = math.sin(d)

elif op == 6:
     d = (a*math.pi)/180
     c = math.cos(d)

elif op == 7:
     d = (a*math.pi)/180
     c = math.tan(d)

elif op == 8:
     d = (a*math.pi)/180
     c = math.cos(d)/math.sin(d)

elif op == 9:
     f=1
     for i in range (1,a+1):
        f = f*i
     c = f

elif op == 10:
     result = math.sqrt(a)
    
print("result=",c)