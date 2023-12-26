import random

count=0
computer_num=random.randint(10,40)
for i in range(10):
    user_num=int(input("enter your number:"))
    if computer_num == user_num :
        count+=1
        print("🎉🎉🎉🎉🎉 win 🎉🎉🎉🎉🎉") 
        print("the number of guess:",count)
        break
    elif computer_num < user_num :
        count+=1
        print("pls guess a lower number")

    elif computer_num>user_num:
        count+=1
        print("pls guess a higher number")
        