from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.handlers.callbackdata.menu import MainMenuCb


def main_menu_keyboard(is_admin: bool) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Кнопка", callback_data=MainMenuCb(action="button").pack()),
        width=1
    )
    if is_admin:
        keyboard.row(
            InlineKeyboardButton(text="Админ панель", callback_data=MainMenuCb(action="admin").pack()),
            width=1
        )
    return keyboard.as_markup()
