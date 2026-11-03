from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.content import EXERCISES
from app.keyboards.inline import exercise_keyboard
from app.database import add_points

router = Router()

class ExerciseState(StatesGroup):
    waiting = State()

@router.callback_query(F.data.startswith("exercise:"))
async def start_exercise(callback: CallbackQuery, state: FSMContext):
    _, course_id, number = callback.data.split(":")
    number = int(number)
    item = EXERCISES.get((course_id, number))
    if not item:
        await callback.answer("Bu mavzu uchun mashq hali qo'shilmagan.", show_alert=True)
        return
    await state.update_data(course_id=course_id, number=number)
    await state.set_state(ExerciseState.waiting)
    await callback.message.answer("✍️ <b>Mashq:</b>\n" + item[0], reply_markup=exercise_keyboard(course_id, number), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data.startswith("answer:"))
async def answer_exercise(callback: CallbackQuery, state: FSMContext):
    _, course_id, number, answer = callback.data.split(":")
    item = EXERCISES.get((course_id, int(number)))
    if not item:
        await callback.answer("Mashq topilmadi.", show_alert=True)
        return
    if answer == item[2]:
        await add_points(callback.from_user.id, 5)
        await callback.message.answer("✅ To'g'ri! +5 ball\n" + item[3])
    else:
        await callback.message.answer("❌ Bu javob noto'g'ri. To'g'ri javob: " + item[2] + "\n" + item[3])
    await state.clear()
    await callback.answer()
