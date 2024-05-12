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
            InlineKeyboardButton(text="Частозадаваемые вопросы", callback_data='dislike')
        ]
    ]
)

keyboard_contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='contacts'),
        ],
        [
            InlineKeyboardButton(text="Написать менеджеру", callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text="Частозадаваемые вопросы", callback_data='dislike')
        ]
    ]
)

