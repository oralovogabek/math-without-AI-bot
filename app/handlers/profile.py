from aiogram import Router, F
from aiogram.types import Message
from app.database import get_user

router = Router()

@router.message(F.text == "👤 Profilim")
async def profile(message: Message):
    user = await get_user(message.from_user.id)
    if not user:
        await message.answer("Avval /start buyrug'ini bosing.")
        return
    await message.answer(
        f"👤 <b>Profil</b>\nIsm: {user['full_name']}\n"
        f"Telegram ID: <code>{user['telegram_id']}</code>\n"
        f"Level: {user['level']}\nBall: {user['points']}",
        parse_mode="HTML"
    )
