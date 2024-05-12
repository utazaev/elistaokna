from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.handlers import message
from aiogram.types import CallbackQuery
from dotenv import load_dotenv
import os
from aiogram.client.bot import DefaultBotProperties

from Keyboards.inlinekeyboards import keyboard_contacts
from handlers.first_menu import get_first_inline_menu
from handlers.get_location import get_location
from handlers.start import get_start
from utils import set_bot_commands

load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('admin_id')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def start_bot():
    await bot.send_message(admin_id, text='Я запустил бота')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands="start"))
dp.callback_query.register(get_location, F.data == "location")
dp.callback_query.register(get_start, F.data == "contacts")
dp.callback_query.register(get_first_inline_menu, F.data == "first_inline_menu")

# dp.message.register(location, F.data == "location")
async def start():
    await set_bot_commands.set_default_commands(bot)  # запуск меню
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
