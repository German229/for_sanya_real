import telebot
import requests
from bs4 import BeautifulSoup

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

Token = "6210204801:AAETGeOSrSxUP_pxWakj7SC84dSBqBs5j5M"
bot = telebot.TeleBot(Token)



keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Информатика'))
keyboard.add(KeyboardButton('Математика'))
keyboard.add(KeyboardButton('Русский язык'))


# Олимпиада по инфе
resp_inf = requests.get("https://mos-inf.olimpiada.ru/?ysclid=lf8o9dbwfn18528500")

html_inf = resp_inf.text

soup_inf = BeautifulSoup(html_inf, "html.parser")

text_inf = soup_inf.body.get_text().strip()


# олимпиада по матеше
resp_mat = requests.get("https://mos.olimpiada.ru/olymp/math?ysclid=lfb905hkgi882582554")

html_mat = resp_mat.text

soup_mat = BeautifulSoup(html_mat, "html.parser")

text_mat = soup_mat.body.get_text().strip()

# олипиада по русскому

resp_rus = requests.get("https://mos.olimpiada.ru/olymp/phil?ysclid=lfbbcso3uf668732770")

html_rus = resp_rus.text

soup_rus = BeautifulSoup(html_rus, "html.parser")

text_rus = soup_rus.body.get_text().strip()


print()






@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, выберете олимпиаду о которой хотите узнать все!', reply_markup=keyboard)


@bot.message_handler(func=lambda s: 'Информатика'in s.text)
def informatica_message(message):
    for elem_inf in text_inf.split('\n')[text_inf.split('\n').index('НОВОСТИ'):text_inf.split('\n').index('29.11.2019 Опубликована информация о Московской олимпиаде по информатике в 2019-2020 уч. году')]:
        bot.send_message(message.chat.id, elem_inf)

    #bot.send_message(message.chat.id, 'Подробнее можно ознакомиться здесь 👇 https://mos-inf.olimpiada.ru/?ysclid=lf8o9dbwfn18528500')


@bot.message_handler(func=lambda n: 'Математика'in n.text)
def math_message(message):
    for elem_mat in text_mat.split('\n')[text_mat.split('\n').index('14 марта'):text_mat.split('\n').index('Архив новостей')]:
        if elem_mat != " ":
            bot.send_message(message.chat.id, elem_mat)
    bot.send_message(message.chat.id, 'Подробнее можно ознакомиться здесь 👇 https://mos.olimpiada.ru/olymp/math?ysclid=lfb905hkgi882582554')

@bot.message_handler(func=lambda m: 'Русский'in m.text)
def rus_message(message):
    for elem_rus in text_rus.split('\n')[text_rus.split('\n').index('28 февраля'):text_rus.split('\n').index('Архив новостей')]:
        if elem_rus != " ":
            bot.send_message(message.chat.id, elem_rus)
    bot.send_message(message.chat.id, 'Подробнее можно ознакомиться здесь 👇 https://mos.olimpiada.ru/olymp/phil?ysclid=lfbbcso3uf668732770')



bot.infinity_polling()