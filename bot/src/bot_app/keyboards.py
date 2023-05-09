from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_kin = InlineKeyboardButton('Кинолог', callback_data='kinolog')
inline_button_user = InlineKeyboardButton('Пользователь', callback_data='user')
inline_kb = InlineKeyboardMarkup()

inline_kb.add(inline_button_kin).add(inline_button_user)

kin_q1 = InlineKeyboardButton('answer 1', callback_data='ans1')
kin_q2 = InlineKeyboardButton('answer 2', callback_data='ans2')
kin_q3 = InlineKeyboardButton('answer 3', callback_data='ans3')

kb_kin_q = InlineKeyboardMarkup()
kb_kin_q.add(kin_q1).add(kin_q2).add(kin_q3)

kin_d1 = InlineKeyboardButton('date time 1', callback_data='date1')
kin_d2 = InlineKeyboardButton('date time 2', callback_data='date2')
kin_d3 = InlineKeyboardButton('date time 3', callback_data='date3')

kb_kin_d = InlineKeyboardMarkup()
kb_kin_d.add(kin_d1).add(kin_d2).add(kin_d3)