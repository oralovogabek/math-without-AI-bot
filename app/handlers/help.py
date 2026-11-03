from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ℹ️ Yordam")
async def help_message(message: Message):
    await message.answer(
        "ℹ️ <b>MathMaster UZ qo'llanmasi</b>\n\n"
        "📚 Darslarni boshlash — level va mavzu tanlash.\n"
        "✍️ Mashq bajarish — dars ichidagi mashq tugmasi.\n"
        "📝 Test ishlash — mini test.\n"
        "➗ Kalkulyator — matematik ifodani yuboring.\n"
        "🎓 Milliy sertifikat — tayyorgarlik savoli.\n"
        "📊 Natijalarim — ball va faollik.",
        parse_mode="HTML"
    )
