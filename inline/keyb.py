from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)

url_button_alex=InlineKeyboardButton(
     text="Алексей",
     callback_data='button_alex'
)
url_button_danila=InlineKeyboardButton(
     text="Данила",
     callback_data='button_d'
)
url_button_gera=InlineKeyboardButton(
     text="Георгий",
     callback_data='button_g'
)
url_button_sasha=InlineKeyboardButton(
     text="Александр",
     callback_data='button_s'
)
keyboard_author=InlineKeyboardMarkup(
     inline_keyboard=[[url_button_alex], [url_button_danila], [url_button_gera], [url_button_sasha]]
)