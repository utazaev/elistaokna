from aiogram import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Контакты", callback_data='location'),
        ],
        [
            InlineKeyboardButton(text="Написать менеджеру", callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data='dislike')
        ]
    ]
)

keyboard_contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='first_inline_menu'),
        ],
        [
            InlineKeyboardButton(text="Написать менеджеру", callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data='dislike')
        ]
    ]
)

