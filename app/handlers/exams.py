from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.inline import exam_keyboard

router = Router()

@router.message(F.text == "🎓 Milliy sertifikat")
async def national_exam(message: Message):
    await message.answer(
        "🎓 Milliy sertifikat tayyorgarlik bo'limi.\n\n"
        "Hozircha namunaviy savol:\n"
        "3 × (8 + 2) − 5 = ?",
        reply_markup=exam_keyboard()
    )
