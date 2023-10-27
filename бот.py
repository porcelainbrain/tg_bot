!pip install pyTelegramBotAPI
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = 'import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6825867085:AAFY41F48q1R0e7tqU_gpu3Hh77H_pU5gCsN'

# Здесь можно использовать API для астрологических прогнозов (замените на реальный URL)
ASTROLOGY_API_URL = 'https://horo.mail.ru/horoscope/zodiac/'

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот астрологических прогнозов. Чтобы получить прогноз, введите /horoscope знак зодиака, например /horoscope Овен.")

# Обработчик команды /horoscope
def horoscope(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 1:
        update.message.reply_text("Пожалуйста, укажите только один знак зодиака после /horoscope, например /horoscope Овен.")
        return

    sign = args[0]
    response = requests.get(f"{ASTROLOGY_API_URL}/{sign}")
    
    if response.status_code == 200:
        horoscope_data = response.json()
        update.message.reply_text(horoscope_data['horoscope'])
    else:
        update.message.reply_text("Извините, не удалось получить астрологический прогноз. Попробуйте позже.")

# Главная функция
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("horoscope", horoscope))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
'

# Здесь можно использовать API для астрологических прогнозов (замените на реальный URL)
ASTROLOGY_API_URL = 'https://api.example.com/astrology'

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я бот астрологических прогнозов. Чтобы получить прогноз, введите /horoscope знак зодиака, например /horoscope Овен.")

# Обработчик команды /horoscope
def horoscope(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 1:
        update.message.reply_text("Пожалуйста, укажите только один знак зодиака после /horoscope, например /horoscope Овен.")
        return

    sign = args[0]
    response = requests.get(f"{ASTROLOGY_API_URL}/{sign}")
    
    if response.status_code == 200:
        horoscope_data = response.json()
        update.message.reply_text(horoscope_data['horoscope'])
    else:
        update.message.reply_text("Извините, не удалось получить астрологический прогноз. Попробуйте позже.")

# Главная функция
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("horoscope", horoscope))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
