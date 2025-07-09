import random

computer_score = 0
user_score = 0

for i in range(3):
    x=random.randint(1, 3)
    computer_choice=x
    user_choice=int(input("enter the number:  1️⃣  2️⃣  3️⃣"))
    print(" 1️⃣ rock")
    print(" 2️⃣ paper")
    print(" 3️⃣ scissors")

    print ("💻:", computer_choice ) 
    print ("👧:", user_choice ) 

    if computer_choice ==1 and user_choice ==1:
        print("you:0 , computer:0")
    elif computer_choice ==1 and user_choice == 2:
        print("you:1🎈 , computer:0")
        user_score+=1
    elif computer_choice == 1 and user_choice == 3:
        print("you:0 , computer:1🎈")
        computer_score+=1
    elif computer_choice == 2 and user_choice == 2:
        print("you:0 , computer:0")
    elif computer_choice == 2 and user_choice == 1:
        print("you:0 , computer:1🎈")
        computer_score+=1
    elif computer_choice == 2 and user_choice == 3:
        print("you:1🎈 , computer:0")
        user_score+=1
    elif computer_choice == 3 and user_choice == 3:
        print("you:0 , computer:0")   
    elif computer_choice == 3 and user_choice == 1:
        print("you:1🎈 , computer:0")
        user_score+=1
    elif computer_choice == 3 and user_choice == 2:
        print("you:0 , computer:1🎈")
        computer_score+=1
        
if computer_score > user_score:
    print("you fail ❌️")
elif user_score > computer_score:
    print("you win ✌️")
elif user_score == computer_score:
    print("try again")
