list = input("enter your list:").split(" ")

if len(list)%2 != 0:
    for i in range(0, (len(list)//2)):
        if list[i] != list[-1-i]:
            print ("not symmetry ❌ ")
            exit()
    print("symmetry ✔") 
else: 
    print ("the length of  your list is odd.")      




       