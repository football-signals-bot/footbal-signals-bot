from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '8042334465:AAFFQZesPcQzSAmxlFxcJ7U_ZZPPEJr_CUY'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я твой футбольный бот ⚽️")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

