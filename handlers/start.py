from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.handlers import message
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Keyboards.inlinekeyboards import keyboard
# from aiogram import types
# from keyboards.register_kb import register_keyboard



photo_url = 'https://lh3.googleusercontent.com/p/AF1QipNFNZRXYGBNts-xvR6akKsO_VzqWnzX_PewNqiA=s680-w680-h510'

start_text = (f'📌 Команда СТРОЙКА.РК более 10 лет на рынке Калмыкии \n✅ Пластиковые окна и алюминиевые конструкции \n✅ Остекление балконов, домов, квартир '
                                 f'\n✅ Входные и межкомнатные двери \n✅ Рассрочка без процентов, монтаж по ГОСТу и качество по доступной цене')
contacts = (f'🧭 Адрес: Республика Калмыкия, ул. Хомутникова, 2А, Элиста, 358000 \n\n Часы работы: \n'
            f'понедельник   09:00–18:00\n'
            f'вторник            09:00–18:00\n'
            f'среда                09:00–18:00\n'
            f'четверг             09:00–18:00\n'
            f'пятница            09:00–18:00\n'
            f'суббота             09:00–18:00\n'
            f'воскресенье    выходной \n\n Телефон: +79374695060')


welcome_message = (f' Здравствуйте 😊 Рады, Вам \n\n '
                    f' Компания Стройка.РК более 17 лет на рынке Элисты и Калмыкии. \n\n'
                   f'За это время мы установили больше 4,5 тысяч окон, рам и дверей и, надеюсь, '
                   f'что в дальнейшем сможем поработать с вами!\n\n'
                   f'Сейчас мы можем предложить:\n\n'
                   f'✅ Пластиковые окна\n'
                   f'✅ Межкомнатные вхоные двери\n'
                   f'✅ Фасадный кипич \n'
                   f'✅ Напольные покрытия\n'
                   f'✅ Кровельные материалы\n\n'
                   f'❓ Что Вас интересует. Выберите вариант, намите на кнопку 👇')
async def get_start(message: Message, bot: Bot):
    await bot.send_photo(message.from_user.id, photo=photo_url
                         )
    await bot.send_message(message.from_user.id, start_text, reply_markup=keyboard)

async def get_menu(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Меню')  # , reply_markup=register_keyboard)

