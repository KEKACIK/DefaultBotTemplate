from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.handlers.callbackdata.admin import AdminCb
from app.bot.handlers.callbackdata.start import GoToCb


def admin_menu_keyboard(_) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=_("buttons.admin_menu_export_users"),
                             callback_data=AdminCb(action="export_users").pack()),
        InlineKeyboardButton(text=_("buttons.back"), callback_data=GoToCb(action="start").pack()),
        width=1
    )
    return keyboard.as_markup()
