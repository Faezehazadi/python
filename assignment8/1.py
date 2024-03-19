import gtts
def read_from_file():
    file = open("F:\Python\Projects\PyLearn-Course\Assignments-8\Translate.txt","r")
    global words_bank
    list = file.read().split("\n")
    words_bank = []
    for i in range(0, len(list), 2):
        dic = {"en": list[i], "fa": list[i+1]}
        words_bank.append(dic)
    file.close()

def write_to_database():
    file = open("F:\Python\Projects\PyLearn-Course\Assignments-8\Translate.txt", "w")
    for word in words_bank:
        new_word_en = word["en"]
        new_word_fa = word["fa"]
        file.write(new_word_en)
        file.write("\n")
        file.write(new_word_fa)
        file.write("\n")
    file.close

def english_to_persian():
    user_text = input("Please Enter your text: ")
    user_words = user_text.split(" ")
    out_put = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                out_put = out_put + word["fa"] + " "
                break
        else:
            out_put = out_put + user_word + " "
    voice = gtts.gTTS(out_put, lang="ar", slow=False)
    voice.save("F:/Python/Projects/PyLearn-Course/Assignments-8/voice-fa.mp3")
    print(out_put)
    print("Also you can hear the voice of your text in (voice-fa) file")

def persian_to_english():
    user_text = input("Please Enter your text: ")
    user_words = user_text.split(" ")
    out_put = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                out_put = out_put + word["en"] + " "
                break
        else:
            out_put = out_put + user_word + " "
    voice = gtts.gTTS(out_put, lang="en", slow=False)
    voice.save("F:/Python/Projects/PyLearn-Course/Assignments-8/voice-en.mp3")
    print(out_put)
    print("Also you can hear the voice of your text in (voice-en) file")
    
def new_word():
    print("Thanks for Helping to Create More Comprehensive Dictionary")
    while True:
        user_new_word_en = input("First add Your New (English) Word: ")
        user_new_word_fa = input("Second add Your New (Persian) Word: ")
        new_word = {"en": user_new_word_en, "fa": user_new_word_fa}
        words_bank.append(new_word)
        end = int(input("If You Have No More New Word Press (1) or Press (2) For Continuing: "))
        if end == 1:
            print("Tanks For Your Helping")
            break

def show_menu():
    print("Hello and Welcome to the Initial Google Sharifan Translate")
    print("1- For Translating (English) to (Persian)")
    print("2- For Translating (Persian) to (English)")
    print("3- For Adding a New Word in to the Database")
    print("4- Exit")

read_from_file()
show_menu()
while True:
    user_choice = int(input("Please Select Your Number: "))
    if user_choice == 1:
        english_to_persian()
    elif user_choice == 2:
        persian_to_english()
    elif user_choice == 3:
        new_word()
    elif user_choice == 4:
        write_to_database()
        exit(0)
    else:
        print("Please Enter a Valid Number from the list")