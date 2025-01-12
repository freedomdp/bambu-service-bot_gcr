from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from src.components.keyboards.reply import get_main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вітаю! Я бот підтримки Bambu Lab Україна 🇺🇦. Оберіть, будь ласка, тему звернення:",
        reply_markup=get_main_menu_keyboard(),
    )

def get_start_handler():
    return CommandHandler("start", start)
