import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from app.config import BOT_TOKEN
from app.database import init_db
from app.handlers import start, courses, lessons, exercises, tests, calculator, exams, progress, profile, help

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

async def health(request):
    return web.json_response({"status": "ok", "service": "MathMaster UZ"})

async def start_web():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", "10000")))
    await site.start()
    return runner

async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi. .env faylini tekshiring.")
    await init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    for router in (start.router, courses.router, lessons.router, exercises.router,
                   tests.router, calculator.router, exams.router,
                   progress.router, profile.router, help.router):
        dp.include_router(router)
    runner = await start_web()
    try:
        logger.info("MathMaster UZ ishga tushdi.")
        await dp.start_polling(bot)
    finally:
        await runner.cleanup()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
