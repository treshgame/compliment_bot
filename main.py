from parse import Parse
import random
from SETTINGS import *
import telebot

parse = Parse(URL)  #create class with pasred dates
i=0
for k in parse.get_content():   #count 
    i+=1

def get_random_message():
    random_i = random.randrange(0, i-1)     
    random_message = parse.compliments[random_i]    #random compliment from array
    return random_message


tgbot = telebot.TeleBot(TOKEN)  #Create bot and give him the token

def creat_keyboard():   
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)    #button will looks good thanks this
    return keyboard

#create a keyboard and button for it
keyboard = creat_keyboard()
keyboard.row(BUTTON_COMPLIMENT)

@tgbot.message_handler(commands=['start'])  #if /start in chat
def start_be_happy(message):
    tgbot.send_message(message.chat.id, "I love you dude, you're awesome", reply_markup = keyboard) #send message in chat and show keyboard
@tgbot.message_handler(content_types=['text'])   #if user send some message
def give_complimet(message):
    if message.text == BUTTON_COMPLIMENT:
        tgbot.send_message(message.chat.id, get_random_message(), reply_markup = keyboard)   #send compliment in chat and show keyboard
    else:
        tgbot.send_message(message.chat.id, 'You pretty but I cant understand', reply_markup = keyboard)

tgbot.polling() #Need for bot's work