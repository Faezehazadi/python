list= []
num = int(input("Enter length of list :"))
for i in range(num):
    list.append(int(input("Enter number:")))
   
print("Without duplicate:", set(list))