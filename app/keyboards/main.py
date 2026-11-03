from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Darslarni boshlash"), KeyboardButton(text="📝 Test ishlash")],
            [KeyboardButton(text="✍️ Mashq bajarish"), KeyboardButton(text="➗ Kalkulyator")],
            [KeyboardButton(text="🎓 Milliy sertifikat"), KeyboardButton(text="📊 Natijalarim")],
            [KeyboardButton(text="👤 Profilim"), KeyboardButton(text="ℹ️ Yordam")],
        ],
        resize_keyboard=True
    )
