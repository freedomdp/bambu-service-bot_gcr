import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Завантаження змінних з .env
load_dotenv()

# Отримання токену з .env
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome to Bambu Lab Service Bot! Choose an option:')

# Основна функція
def main() -> None:
    # Створення додатку
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Додавання обробника команди /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
