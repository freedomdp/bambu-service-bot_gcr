from telegram import ReplyKeyboardMarkup

def get_main_menu_keyboard():
    keyboard = [["🔧 Поломка", "🖨 Якість друку"], ["❓ Питання / Відповідь"]]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
