
import telebot
from flask import Flask, request
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать.')


@app.route('/', methods=['POST', 'GET'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'Test Bot', 200


@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='????????')
    return 'Test Bot', 200

