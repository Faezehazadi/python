
import random
import requests
import telebot
from telebot import types
from khayyam import JalaliDate
import gtts
import qrcode

bot=telebot.TeleBot("",parse_mode=None)
game_number = None  
flag=None
win=False

bot_keyboard = types.ReplyKeyboardMarkup(row_width=2)
key1 = types.KeyboardButton("/start")
key2 = types.KeyboardButton('/game')
key3 = types.KeyboardButton('/age')
key4 = types.KeyboardButton('/voice')
key5 = types.KeyboardButton('/max')
key6 = types.KeyboardButton('/argmax')
key7 = types.KeyboardButton('/qrcode')
key8 = types.KeyboardButton('/help')
bot_keyboard.add(key1, key2, key3, key4, key5, key6, key7, key8)


def create_game_keyboard():
    game_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    new_game_key = types.KeyboardButton('/newgame')
    exit_key = types.KeyboardButton('/exit')
    game_keyboard.add(new_game_key, exit_key)
    return game_keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global flag
    flag="start"
    first_name = message.from_user.first_name
    bot.reply_to(message," 🔺 Welcome "+str(first_name)+" to FaezehAzadiBOT 🔻",reply_markup=bot_keyboard)


@bot.message_handler(commands=['game'])
def game(message):
    global flag
    global win
    flag="game"
    win=False
    global game_number
    game_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "🔸 Guess the Number Game 🎲 ", reply_markup=create_game_keyboard())


@bot.message_handler(func=lambda message: message.text == '/newgame')
def new_game(message):
    global flag
    global win
    flag="game"
    win=False
    global game_number
    game_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "🔸 Guess a number between 1 - 100 🎲 ", reply_markup=create_game_keyboard())


@bot.message_handler(func=lambda message: message.text == '/exit')
def exit_game(message):
    global game_number
    game_number = None
    global win
    win=False
    bot.send_message(message.chat.id, " ✌ The end ✌ ", reply_markup=bot_keyboard)


@bot.message_handler(commands=['age'])
def calculate_age(message):
    global flag
    flag="age"
    bot.send_message(message.chat.id, "🔸 Enter your birthdate - yyyy/mm/dd ", reply_markup=bot_keyboard)
    

@bot.message_handler(commands=['voice'])
def send_voice(message):
    global flag
    flag="voice"
    bot.send_message(message.chat.id, "🔸 Enter your English sentence 🎵")


@bot.message_handler(commands=['max'])
def find_max(message):
    global flag
    flag="max"
    bot.send_message(message.chat.id, "🔸 Enter your list of numbers:  1️⃣ .  2️⃣ .  3️⃣ ")


@bot.message_handler(commands=['argmax'])
def find_argmax(message):
    global flag
    flag="argmax"
    bot.send_message(message.chat.id, "🔸 Enter your list of numbers:  1️⃣ .  2️⃣ .  3️⃣")


@bot.message_handler(commands=['qrcode'])
def generate_qrcode(message):
    global flag
    flag="qrcode"
    bot.send_message(message.chat.id, "🔸 Enter your string: ")


@bot.message_handler(commands=['help'])
def display_help(message):
    send_help_message(message)  


@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    if flag=="game":
        global game_number
        global win
        win=False
        count=1
        try:
            if count<=10 and win==False:
                guess = int(message.text)
                if guess < game_number:
                    bot.reply_to(message, "🔸 go up ⬆ ")
                elif guess > game_number:
                    bot.reply_to(message, "🔸 go down ⬇ ")
                else:
                    bot.reply_to(message, "🔸 you win 🎈")
                    game_number = None
                    win=True
                count+=1
            elif win==True:
                bot.send_message(message.chat.id, "🔸 Do you want to play again? ", reply_markup=create_game_keyboard())
                
            else:
                win=False
                bot.reply_to(message, f"🔸 You lost ☹ . the true number is: {game_number}")
                bot.send_message(message.chat.id, "🔸 Do you want to play again? ", reply_markup=create_game_keyboard())
        except ValueError:
            bot.reply_to(message, "🔸 You can only enter numbers. ❌ ")
    
    elif flag=="age":
        try:
            birthday = (message.text)
            birth_year, birth_month, birth_day = map(int, birthday.split('/'))

            today = JalaliDate.today()
        
            age = today.year - birth_year - 1 if (today.month, today.day) < (birth_month, birth_day) else today.year - birth_year
            month = today.month - birth_month if today.month >= birth_month else 12 - birth_month + today.month
            day = today.day - birth_day if today.day >= birth_day else JalaliDate(today.year, today.month - 1, today.day).days_in_month - birth_day + today.day
            
            bot.send_message(message.chat.id,f"🔸 your age {age} years and  {month} month and {day} days. " )

        except ValueError:
            bot.send_message(message.chat.id,"🔸 is not correct. Enter your birthdate - yyyy/mm/dd)")


    elif flag=="voice":
        text = (message.text) 
        x = gtts.gTTS(text, lang="en", slow=False)
        x.save("voice.mp3") 
            

        audio_file = open("voice.mp3", "rb")
        bot.send_voice(message.chat.id, audio_file)
        audio_file.close()
    

    elif flag=="max":      
        text = (message.text) 
        numbers = text.split('.')
        numbers = [int(num.strip()) for num in numbers]
        max_value = max(numbers)
        bot.send_message(message.chat.id, f"🔸 The Maximum number is : {max_value}")
 

    elif flag=="argmax":
        text=(message.text)
        numbers = text.split('.')
        numbers = [int(num.strip()) for num in numbers]
        max_index = numbers.index(max(numbers))
        bot.send_message(message.chat.id, f"🔸 The index of the maximum number is: {max_index}")
    

    elif flag=="qrcode":
        text=(message.text)
        img_QR = qrcode.make(text)
        img_QR.save("QrCode.png")

        qr_file=open("QrCode.png","rb")
        bot.send_photo(message.chat.id, qr_file)     
 

def send_help_message(message):
    help_text = '''
    🔸 start: Greet with the user's name.
    🔸 game: Guess a random number game.
    🔸 age: Calculate your age.
    🔸 voice: Convert a eng sentence to voice.
    🔸 max: Find the maximum number. 
    🔸 argmax: Find the index of the max number.
    🔸 qrcode: Make a QR code from the input text.
    🔸 help: Display help message.'''

    bot.send_message(message.chat.id, help_text)

bot.infinity_polling()