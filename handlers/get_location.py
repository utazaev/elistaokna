from aiogram import Bot, F
from aiogram.types import CallbackQuery, Message
from Keyboards.inlinekeyboards import keyboard, keyboard_contacts
from handlers.start import photo_url, start_text


async def get_location(call: CallbackQuery, bot: Bot):
    await call.message.edit_text(text=start_text, chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=keyboard_contacts)
    #await call.message.answer_photo(photo=photo_url, caption='Телефон адрес', reply_markup=keyboard_contacts)
    await call.answer()
    # await bot.send_location(call.message.answer, 46.312108, 44.252802)

# async def location(call: CallbackQuery, bot: Bot):

