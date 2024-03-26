length_array=int(input("Enter the length of the array : "))
araye = []

for i in range (length_array) :
    num=int(input("enter the num: "))
    araye.append(num)   
print ("sort of array: " , sorted(araye))
