from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
import wttr

load_dotenv()
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Hello. This is a bot for weather forecast')
    await message.answer("Write the city name to get the weather")

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer("Write the city name to get the weather")

@dp.message()
async def send_weather(message: Message):
    city = message.text.strip()
    weather_data = wttr.get_weather(city)
    if weather_data['text']:
        await message.answer(weather_data['tooltip'], parse_mode="HTML")
    else:
        await message.answer(weather_data['tooltip'])

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot))
#    dp.run_polling(bot)
