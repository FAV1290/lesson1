import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(filename='bot.log', level=logging.INFO)
VERSION = '0.2.2-alpha'


def my_version(update, context):
    print('Вызвана команда /verson')
    update.message.reply_text(f'Привет! Это версия бота №{VERSION}')    


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def greet_user(update, context):
    print('Вызвана команда /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("version", my_version))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot has started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()