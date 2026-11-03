from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.content import COURSES
from app.keyboards.inline import lesson_keyboard
from app.database import add_points

router = Router()

@router.callback_query(F.data.startswith("lesson:"))
async def show_lesson(callback: CallbackQuery):
    parts = callback.data.split(":")
    if len(parts) != 3:
        await callback.answer("Dars ma'lumotida xatolik.", show_alert=True)
        return
    course_id = parts[1]
    try:
        number = int(parts[2])
    except ValueError:
        await callback.answer("Dars raqami noto'g'ri.", show_alert=True)
        return
    if course_id not in COURSES or not 1 <= number <= len(COURSES[course_id][1]):
        await callback.answer("Dars topilmadi.", show_alert=True)
        return
    title, theory, example, formula = COURSES[course_id][1][number - 1]
    text = (
        f"📚 <b>{title}</b>\n\n📖 <b>Nazariya:</b>\n{theory}\n\n"
        f"🧮 <b>Misol:</b>\n{example}\n\n📌 <b>Formula:</b>\n<code>{formula}</code>"
    )
    await callback.message.answer(text, reply_markup=lesson_keyboard(course_id, number), parse_mode="HTML")
    await add_points(callback.from_user.id, 1, lesson=True)
    await callback.answer("Dars ochildi! +1 ball")
