from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='15 seconds', callback_data='seconds:15'), InlineKeyboardButton(text='30 seconds', callback_data='seconds:30')],
        [InlineKeyboardButton(text='60 seconds', callback_data='seconds:60'), InlineKeyboardButton(text='120 seconds', callback_data='seconds:120')]
    ]
)