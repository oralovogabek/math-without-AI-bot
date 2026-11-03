# MathMaster UZ

Python + aiogram 3 asosidagi matematik ta'lim Telegram botining boshlang'ich ishlaydigan loyihasi.

## Windows / PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

`.env` faylida `BOT_TOKEN` qiymatini BotFather bergan token bilan almashtiring.

Ishga tushirish:

```powershell
python -m app.main
```

## Eslatma
- Darslar sakkizta levelga ajratilgan.
- Barcha darslar ko'rinadi; hozircha ayrim darslargagina namunaviy mashqlar kiritilgan.
- SQLite ma'lumotlar bazasi lokal ishga tushirish uchun qulay. Render'da doimiy saqlash uchun persistent disk yoki PostgreSQL kerak.
- Milliy sertifikat bo'limidagi savollar hozircha demo; rasmiy imtihonning to'liq savollar banki emas.
