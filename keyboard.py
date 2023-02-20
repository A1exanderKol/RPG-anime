from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


B2 = KeyboardButton('/SHOW')
B3 = KeyboardButton('/PROFILE')

kb = ReplyKeyboardMarkup()
kb.add(B2)
kb.add(B3)