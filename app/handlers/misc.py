from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("cancel"))
async def cancel_any(message: Message):
    await message.answer("Joriy amal bekor qilindi.")
