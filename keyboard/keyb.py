import aiogram
from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup


bu_game=KeyboardButton(text='Игра🎮')
bu_rask=KeyboardButton(text="Раскраска")
bu_stick=KeyboardButton(text="Стикеры")
bu_music=KeyboardButton(text="Беларусская Музыка🎼")
bu_author=KeyboardButton(text="Авторы🎬")
nu_like=KeyboardButton(text="❤️")
nu_dislike=KeyboardButton(text="👎")
bu_buy=KeyboardButton(text="Закрасить")
ras=KeyboardButton(text="Раскраска")
top_game=KeyboardButton(text='ТОП-игроков')


k_buy=[[bu_buy, ras]]
rask=[[ras]]
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'{i}') for i in range(1, 21)]
key=[[buttons[0], buttons[1], buttons[2], buttons[3], buttons[4]],[buttons[5], buttons[6], buttons[7], buttons[8], buttons[9]], [buttons[10], buttons[11], buttons[12], buttons[13], buttons[14]], [buttons[15], buttons[16], buttons[17], buttons[18], buttons[19]]]

num_key=ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True, input_field_placeholder="Выберите кнопку")
kb_menu=ReplyKeyboardMarkup(keyboard=[[bu_music], [bu_game, bu_stick, bu_rask], [top_game, bu_author]], resize_keyboard=True, input_field_placeholder="Выберите действие")
like_menu=ReplyKeyboardMarkup(keyboard=[[nu_like, nu_dislike]], input_field_placeholder="Как вам трек?", resize_keyboard=True)
raska=ReplyKeyboardMarkup(keyboard=rask, input_field_placeholder="Как вам трек?", resize_keyboard=True)
num_buy=ReplyKeyboardMarkup(keyboard=k_buy, resize_keyboard=True, input_field_placeholder="Выберите кнопку")