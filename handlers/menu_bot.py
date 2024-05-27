from aiogram import Bot
from aiogram.types import CallbackQuery
from Keyboards.inlinekeyboards import keyboard_menu_price
from handlers.start import welcome_message

async def get_menu_price(call: CallbackQuery, bot: Bot):
    await call.message.edit_text(text=welcome_message, reply_markup=keyboard_menu_price)
    await call.answer()
