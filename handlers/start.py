from aiogram import Bot
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.inlinekeyboards import keyboard
# from aiogram import types
# from keyboards.register_kb import register_keyboard



photo_url = 'https://lh3.googleusercontent.com/p/AF1QipNFNZRXYGBNts-xvR6akKsO_VzqWnzX_PewNqiA=s680-w680-h510'

start_text = (f'📌 Команда СТРОЙКА.РК более 10 лет на рынке Калмыкии \n✅ Пластиковые окна и алюминиевые конструкции \n✅ Остекление балконов, домов, квартир '
                                 f'\n✅ Входные и межкомнатные двери \n✅ Рассрочка без процентов, монтаж по ГОСТу и качество по доступной цене')
contacts = f'Адрес: ул. Хомутникова, 2А, Элиста, Респ. Калмыкия, 358000 \n\n Часы работы: пн-сб 09:00–18:00, воскресенье-выходной \n\n Телефон: +79374695060'


async def get_start(message: Message, bot: Bot):
    await bot.send_photo(message.from_user.id, photo=photo_url
                         )
    await bot.send_message(message.from_user.id, start_text, reply_markup=keyboard)

async def get_menu(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Меню')  # , reply_markup=register_keyboard)

