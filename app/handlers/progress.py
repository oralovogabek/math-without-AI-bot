from aiogram import Router, F
from aiogram.types import Message
from app.database import get_user

router = Router()

@router.message(F.text == "📊 Natijalarim")
async def progress(message: Message):
    user = await get_user(message.from_user.id)
    if not user:
        await message.answer("Avval /start buyrug'ini bosing.")
        return
    await message.answer(
        f"📊 <b>Natijalaringiz</b>\n\n⭐ Ballar: {user['points']}\n"
        f"📚 Ochilgan darslar: {user['lessons_done']}\n"
        f"📝 To'g'ri testlar: {user['tests_done']}",
        parse_mode="HTML"
    )
