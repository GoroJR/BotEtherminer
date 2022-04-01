# importing the requests library and pprint
import os
from pprint import pprint
import telebot
from Constants import *
import requests



# creacion del bot asocido con mi key creado por BotFather
bot = telebot.TeleBot({"Telegram BOT ID"})


def get_unpaid():
    req = requests.get(URL_ETH)
    data_json_eth = req.json()
    data_eth = dict(data_json_eth)
    # 2288 on january 2021
    ETH2USD = int(float(data_eth['data']['amount']))

    # sending get request and saving the response as response object
    r = requests.get(URL)

    # extracting data in json format
    data_json = r.json()
    data = dict(data_json)

    format_unpaid = int(data['data']['unpaid']) * 10e-19
    usd = format_unpaid * ETH2USD
    return ('USD: ' + str(usd) + '\nETH-USD: ' + str(ETH2USD))


def get_hash():
    # sending get request and saving the response as response object
    r = requests.get(URL)

    # extracting data in json format
    data_json = r.json()
    data = dict(data_json)

    return ('Average Hashrate: ' + str(10e-7 * round(int(data['data']['averageHashrate'])))) + (
            '\nMy Hashrate: ' + str(10e-7 * round(int(data['data']['currentHashrate']))))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Usa /pay para ver el precio del dolar vs etherum y el saldo pendiente por cobrar minado"
                          "o usa /hash para ver el average de hash rate vs el tuyo")


@bot.message_handler(commands=['pay'])
def get_pay(message):
    info = get_unpaid()
    bot.reply_to(message, info)


@bot.message_handler(commands=['hash'])
def get_pay(message):
    info = get_hash()
    bot.reply_to(message, info)


'''@bot.message_handler(commands=['temp'])
def get_temp(message):
    os.system('Alice.py')
    bot.send_photo(680407221, photo=open('example.png', 'rb'))
'''

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,
                 'Este comando no es reconocido, porfavor usa /start o /help para empezar, si te llemas Itzel Vega te amo ')


bot.polling(non_stop=True)
