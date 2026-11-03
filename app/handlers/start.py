from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.database import register_user
from app.keyboards.main import main_menu

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await register_user(message.from_user)
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! 👋\n\n"
        "MathMaster UZ botiga xush kelibsiz!\n"
        "Matematikani bosqichma-bosqich o'rganamiz.",
        reply_markup=main_menu()
    )
