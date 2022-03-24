import random
import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - пока что тупой бот, но что-то умею".format(message.from_user, bot.get_me()))
	murkup = types.ReplyKeyboardMarkup(resize_keyboard=False)
	item1 = types.KeyboardButton("Рандомное число")
	item2 = types.KeyboardButton("Как у тебя дела?")
	murkup.add(item1, item2)
	bot.send_message(message.chat.id, "А ну ка, тыкни на кнпочку", parse_mode='html', reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def knopki(message):
	if message.chat.type == 'private':
		if message.text == 'Рандомное число':
			bot.send_message(message.chat.id, str(random.randint(0, 100)))
		elif message.text == 'Как у тебя дела?':
			bot.send_message(message.chat.id, "Лучше всех!!!")
		else:
			bot.send_message(message.chat.id, "Моя твоя не понимать")

bot.polling( none_stop=True )