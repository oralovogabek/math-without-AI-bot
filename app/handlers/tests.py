from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards.inline import exam_keyboard
from app.database import add_points

router = Router()

@router.message(F.text == "📝 Test ishlash")
async def test_start(message: Message):
    await message.answer("📝 Mini test\n\n10 + 5 × 1 = ?", reply_markup=exam_keyboard())

@router.callback_query(F.data.startswith("exam:"))
async def test_answer(callback: CallbackQuery):
    answer = callback.data.split(":")[1]
    if answer == "B":
        await add_points(callback.from_user.id, 10, test=True)
        await callback.message.answer("✅ To'g'ri! 10 + 5 × 1 = 15. Sizga 10 ball berildi.")
    else:
        await callback.message.answer("❌ Noto'g'ri. To'g'ri javob: B) 15.")
    await callback.answer()
