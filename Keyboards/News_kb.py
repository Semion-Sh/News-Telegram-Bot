from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

inline_btn_publish = InlineKeyboardButton('Опубликовать', callback_data='publish')
inline_btn_delete = InlineKeyboardButton('Удалить', callback_data='cancel')
# inline_btn_change = InlineKeyboardButton('Изменить', callback_data='change')


inline_kb = InlineKeyboardMarkup().add(inline_btn_publish, inline_btn_delete)