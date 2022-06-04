import telebot
from petshop.settings import BOT_TOKEN, BOT_CHAT_ID
from celery import shared_task

bot = telebot.TeleBot(BOT_TOKEN)

@shared_task
def send_registration_notification():
    bot.send_message(BOT_CHAT_ID, "New user!")
