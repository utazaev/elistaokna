from aiogram import Bot, F
from aiogram.types import CallbackQuery, Message
from Keyboards.inlinekeyboards import keyboard, keyboard_contacts
from handlers.start import photo_url, start_text, contacts


async def get_first_inline_menu(call: CallbackQuery, bot: Bot):
    await call.message.edit_text(text=start_text, reply_markup=keyboard)
    await call.answer()