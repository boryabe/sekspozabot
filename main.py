import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "https://api.telegram.org/bot8149028973:AAGWM4WEo0C8V8KKRKU-XaC5I4P4EAYKf6E"  # o'zing olgan tokenni shu yerga qo'y

# Poza nomlari ro'yxati
pozalar = [
    "Missioner", "Doggy style", "Cowgirl", "Reverse cowgirl",
    "Lotus", "Spooning", "Standing", "Butterfly", "Bridge", "Wheelbarrow"
]

# Logger
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men Seks Poza Lotoreya botiman.\n\nPoza olish uchun /poza deb yoz.")

@dp.message_handler(commands=["poza"])
async def send_random_poza(message: types.Message):
    poza = random.choice(pozalar)
    await message.reply(f"Bugungi poza: *{poza}*", parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
