from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# توکن ربات تلگرام از BotFather
TOKEN = "8128388686:AAFUEWryu4boPZHYEFa0-i3IjTWPfgiU-d0"

# لینک صفحه لندینگ / Web App
WEB_APP_URL = "https://storage.googleapis.com/your-bucket-name/index.html"

# دستور /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("باز کردن لندینگ", web_app={"url": WEB_APP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("سلام 👋! برای بازدید از لندینگ روی دکمه زیر کلیک کنید:", reply_markup=reply_markup)

# راه‌اندازی ربات
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
