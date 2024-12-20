import telebot
from config import botkey
bot = telebot.TeleBot(botkey)

@bot.message_handler(commands=['start'])
def handle_message(message):
  bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(command=['help'])
def handler_message(message):
  bot.send_message(message.chat.id, 'Test - BOT!')
bot.polling()
