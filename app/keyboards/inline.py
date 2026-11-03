from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.content import COURSES, EXERCISES

def courses_keyboard():
    rows = []
    for key, (title, lessons) in COURSES.items():
        rows.append([InlineKeyboardButton(text=f"{title} ({len(lessons)} dars)", callback_data=f"course:{key}")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def lessons_keyboard(course_id):
    lessons = COURSES[course_id][1]
    rows = []
    for i, lesson in enumerate(lessons, 1):
        rows.append([InlineKeyboardButton(text=f"{i}. {lesson[0]}", callback_data=f"lesson:{course_id}:{i}")])
    rows.append([InlineKeyboardButton(text="⬅️ Level tanlash", callback_data="courses")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def lesson_keyboard(course_id, number):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✍️ Shu mavzudan mashq", callback_data=f"exercise:{course_id}:{number}")],
        [InlineKeyboardButton(text="⬅️ Darslar ro'yxati", callback_data=f"course:{course_id}")],
    ])

def exercise_keyboard(course_id, number):
    item = EXERCISES.get((course_id, number))
    if not item:
        return None
    options = item[1]
    letters = "ABCD"
    rows = [[InlineKeyboardButton(text=f"{letters[i]}) {v}", callback_data=f"answer:{course_id}:{number}:{letters[i]}")]
            for i, v in enumerate(options)]
    return InlineKeyboardMarkup(inline_keyboard=rows)

def exam_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A) 12", callback_data="exam:A"),
         InlineKeyboardButton(text="B) 15", callback_data="exam:B")],
        [InlineKeyboardButton(text="C) 18", callback_data="exam:C"),
         InlineKeyboardButton(text="D) 20", callback_data="exam:D")]
    ])
