import telebot
import webbrowser

bot = telebot.TeleBot('7869614563:AAFAAueC691ofUYGVv6QAnVh5bp0QWpQEAY')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.16personalities.com/ru/test-lichnosti')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)