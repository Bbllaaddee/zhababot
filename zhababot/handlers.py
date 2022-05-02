import telebot

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, "Sup")

@bot.message_handler()

@bot.message_handler(commands=['ZHABA', 'zhaba', 'Zhaba'])
def zhaba(message):
    chat_id = message.chat.id
    bot.send_picture(chat_id, random_zhaba())
