from aiogram import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍 Контакты", callback_data='location', row_width=1),
        ],
        [
            InlineKeyboardButton(text="🔥 Узнать цену", callback_data='menu_price', row_width=1)
        ],
        [
            InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data='dislike', row_width=1)
        ]
    ]
)

keyboard_contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data='first_inline_menu', row_width=1),
        ],
        [
            InlineKeyboardButton(text="🔥 Узнать цену", callback_data='menu_price', row_width=1)
        ]
    ]
)
keyboard_menu_price = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🪟 Окна", callback_data='dislike', row_width=1),
        ],
        [
            InlineKeyboardButton(text="🚪 Двери", callback_data='dislike', row_width=1)
        ],
        [
            InlineKeyboardButton(text="🧱 Фасадный кирпич", callback_data='dislike', row_width=1)
        ],
        [
            InlineKeyboardButton(text="🟫 Напольные покрытия", callback_data='dislike', row_width=1)
        ],
        [
            InlineKeyboardButton(text="⛺ Кровля", callback_data='dislike', row_width=1)
        ],
        [
            InlineKeyboardButton(text="☎ Консультация", callback_data='dislike', row_width=1)
        ],
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data='first_inline_menu', row_width=1),
        ]
    ]
)

