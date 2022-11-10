import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL: str = 'https://www.tourbaza.com.ua/smishni-anekdoty/'
URL2: str = 'https://www.etnosvit.com/uk/anekdoty_uk.html'



API_KEY: str = '5534930603:AAHtizIwNlx9h0pHRZgAZsnWSpv7KlBFJOU'


def parser(url):

    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='gdlr-core-pbf-element')
    return [c.text for c in anekdots]

def parser2(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
  
    anekdots = soup.find_all('div',class_='sue-panel')

    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
list_of_jokes2 = parser2(URL2)
random.shuffle(list_of_jokes)
rand=random.randint(0,2)
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Добридень, щоб посміятися введіть цифру від 1 до 10')

@bot.message_handler(content_types=['text'])
def jokes(message):
    global rand
    if message.text.lower() in '1234567890':
        if rand == 1:
            bot.send_message(message.chat.id,list_of_jokes[0])
            random.shuffle(list_of_jokes)
            rand=random.randint(0,2)
        else:
            bot.send_message(message.chat.id,list_of_jokes2[0])
            random.shuffle(list_of_jokes2)
            rand=random.randint(0,2)
    else:
        bot.send_message(message.chat.id,'Добридень, щоб посміятися введіть цифру від 1 до 10')
bot.polling()
