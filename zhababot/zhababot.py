import telebot
import os
import random
from dotenv import load_dotenv

def random_zhaba():
    files = os.listdir('./ZHABA/')
    choice = random.choice(files)
    return open(f'./ZHABA/{choice}', 'rb')

def random_zhabapoezd():
    files = os.listdir('./ZHABA_POEZD/')
    choice = random.choice(files)
    return open(f'./ZHABA_POEZD/{choice}', 'rb')

load_dotenv()
token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    reply = "Use /ZHABA for random zhaba! \
            Use /ZHABAPOEZD for random zhapapoezd!"
    bot.reply_to(message, reply)

@bot.message_handler(commands=['ZHABAPOEZD', 'zhabapoezd', 'Zhabapoezd'])
def zhabapoezd(message):
    chat_id = message.chat.id
    bot.send_photo(chat_id, random_zhabapoezd())

@bot.message_handler(commands=['ZHABA', 'zhaba', 'Zhaba'])
def zhaba(message):
    chat_id = message.chat.id
    bot.send_photo(chat_id, random_zhaba())

bot.infinity_polling()
