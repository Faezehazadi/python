num = int(input("enter the num:"))
n1, n2 = 0, 1
count = 0

if num <= 0:
   print("enter a positive number.")
elif num == 1:
   print("Fibonacci sequence:", n1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1