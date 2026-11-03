from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.content import COURSES
from app.keyboards.inline import courses_keyboard, lessons_keyboard

router = Router()

@router.message(F.text == "📚 Darslarni boshlash")
async def show_courses(message: Message):
    await message.answer("📚 O'zingizga kerakli levelni tanlang:", reply_markup=courses_keyboard())

@router.callback_query(F.data == "courses")
async def back_courses(callback: CallbackQuery):
    await callback.message.edit_text("📚 Levelni tanlang:", reply_markup=courses_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith("course:"))
async def show_course(callback: CallbackQuery):
    course_id = callback.data.split(":")[1]
    if course_id not in COURSES:
        await callback.answer("Level topilmadi.", show_alert=True)
        return
    title, lessons = COURSES[course_id]
    await callback.message.edit_text(
        f"{title}\n\nBu levelda {len(lessons)} ta dars mavjud. Darsni tanlang:",
        reply_markup=lessons_keyboard(course_id)
    )
    await callback.answer()
