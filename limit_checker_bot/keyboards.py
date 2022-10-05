from aiogram import types

menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
card_info_button = types.KeyboardButton(text="Отримати інформацію про карти")
# limits_button = types.KeyboardButton(text="Ліміти")
add_new_cards_button = types.KeyboardButton(text="Додати файл з картками")
menu_keyboard.add(card_info_button).add(add_new_cards_button)


back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton(text="Назад")
back_keyboard.add(back_button)


is_correct_keyboard = types.InlineKeyboardMarkup()
yeas_button = types.InlineKeyboardButton(text="Так", callback_data="1")
no_button = types.InlineKeyboardButton(text="Ні", callback_data="0")
is_correct_keyboard.add(yeas_button, no_button)

