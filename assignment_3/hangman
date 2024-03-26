import random

Words_Bank = ["kitten", "cat", "dog", "rabbit", "bee", "owl", "penguin", "butterfly"]

mistakes= 0
corrects= 0

good_chars= []
bad_chars= []

x = random.randint(0, len(Words_Bank)-1)
word = (Words_Bank[x])
counter = len(word)

while mistakes < 6 :
    for i in range(len(word)):
        if word[i] in good_chars:
             print(word[i], end = " ")
        else:
            print("_ ", end = " ")
    if counter == 0:
        print("You win.💯")
        break

    user_char = input("enter your character:")
    user_char = user_char.lower()
    if len(user_char) == 1:
        if user_char in word:
            print("✅️")
            counter = counter-1
            good_chars.append(user_char)
        else:
            print("❎️")
            mistakes += 1
            bad_chars.append(user_char)
    else:
        print("enter one character: ")
if mistakes ==6:
    print("You lose.☠️")