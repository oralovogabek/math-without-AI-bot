import aiosqlite
from app.config import DATABASE_PATH

async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                username TEXT,
                level TEXT DEFAULT 'Foundation',
                points INTEGER DEFAULT 0,
                lessons_done INTEGER DEFAULT 0,
                tests_done INTEGER DEFAULT 0
            )
        """)
        await db.commit()

async def register_user(user):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """INSERT INTO users (telegram_id, full_name, username)
               VALUES (?, ?, ?)
               ON CONFLICT(telegram_id) DO UPDATE SET
               full_name=excluded.full_name, username=excluded.username""",
            (user.id, user.full_name, user.username)
        )
        await db.commit()

async def get_user(telegram_id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        cur = await db.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
        row = await cur.fetchone()
        return dict(row) if row else None

async def add_points(telegram_id, points, lesson=False, test=False):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """UPDATE users SET points=points+?,
               lessons_done=lessons_done+?, tests_done=tests_done+?
               WHERE telegram_id=?""",
            (points, int(lesson), int(test), telegram_id)
        )
        await db.commit()
