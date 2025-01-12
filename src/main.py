import os
from dotenv import load_dotenv
from telegram.ext import Application
from src.handlers.start_handler import get_start_handler

# Загрузка переменных окружения
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def post_init(application: Application):
    await application.bot.set_webhook(url=f"https://your-domain.com/{TELEGRAM_TOKEN}")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).post_init(post_init).build()

    # Регистрация обработчиков
    application.add_handler(get_start_handler())

    # Запуск бота на вебхуках
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=f"https://your-domain.com/{TELEGRAM_TOKEN}",
    )

if __name__ == "__main__":
    main()
