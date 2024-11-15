import aiogram
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

bu_game=KeyboardButton(text='Игра🎮')
bu_stick=KeyboardButton(text="Раскраска")
bu_music=KeyboardButton(text="Беларусская Музыка🎼")
bu_author=KeyboardButton(text="Авторы🎬")
nu_like=KeyboardButton(text="❤️")
nu_dislike=KeyboardButton(text="👎")


kb_menu=ReplyKeyboardMarkup(keyboard=[[bu_music], [bu_game, bu_stick], [bu_author]], resize_keyboard=True, input_field_placeholder="Выберите действие")
like_menu=ReplyKeyboardMarkup(keyboard=[[nu_like, nu_dislike]], input_field_placeholder="Как вам трек?", resize_keyboard=True)