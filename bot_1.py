
from extensions import ConvertionException,CryptoConvector
from const import TOKEN,keys
import telebot



bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f"Доброго времени суток, {message.chat.username}.\n " \
           f"Я помогу узнать актуальные курсы валют. Доступные валюты /values\n Введите через пробел <ИМЯ ВАЛЮТЫ>\n" \
           f"Потом <ВАЛЮТУ, В КОТОРУЮ ПЕРЕВОДИТЬ> \n и <КОЛЛИЧЕСТВО ВАЛЮТЫ>, которое хотите обменять"

    foto = open(r"H:\FILES\SBOXWON-xEQ.jpg", "rb")
    bot.send_photo(message.chat.id, photo=foto)
    bot.send_message(message.chat.id,  text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConvertionException(f'Чего-то не хватает или много параметров!\n Прочесть инструкцию бота можно /help')



        awl, soap, amount = values
        awl, soap = awl.lower(), soap.lower()
        resoult = CryptoConvector.conver(awl, soap, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду.\n {e}")
    else:
        text = f"Цена {amount} {awl} в {soap} - {resoult}"
        bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)

