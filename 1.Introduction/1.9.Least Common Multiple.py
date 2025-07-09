num_1=int(input("enter first number: "))
num_2=int(input("enter second number: "))
j=(num_1 *num_2)+1

if num_1 != 0 and num_2 != 0:
    if (num_1)>(num_2):
            n=(num_1)
    else:
            n=(num_2)

    for i in range(n,j):
        if i%(num_1)== 0 and i%(num_2)== 0:
            Kmm=i
            break
else:
      if num_2 !=0:
            Kmm=num_2
      else:
            Kmm=num_1     
print("Least Common Multiple: ", Kmm) 