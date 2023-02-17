
import telebot

from Config_bot import keys, TOKEN
from utile_bot import ConvertionExeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)

# Функционал бота

@bot.message_handler(commands=['start', 'help']) # Инструкция пользователя
def help(message:telebot.types.Message):
    text = 'Ведите команду в формате: \n<имя валюты>\ <в какуювалюту перевести>\<значение валюты>\
<Можно увидеть список доступных валют командой "values">'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values']) # Справка по валютам
def values(message:telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message): # Проверка соответствия ввода
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Количество пораметров не соответствует 3м.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionExeption as e:         # Обработчик по ошибкам ввода
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:                  # Обработчик по командам
        bot.reply_to(message, f'Не удалось обработать команду. \n{e}')

    else:
        i_total_base = int(total_base)
        i_amount = int(amount)
        i_total_base = i_amount * i_total_base
        total_base = str(i_total_base)

        text = f'Цена {amount} {quote} в {base} - {total_base}' # вывод ответа в опр. виде
        bot.send_message(message.chat.id, text)

bot.polling()
# bot.polling(none_stop=True)