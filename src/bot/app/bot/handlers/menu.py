from aiogram import F, Router
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.bot.handlers.callbackdata.menu import GoToCb
from app.bot.handlers.keyboards.menu import main_menu_keyboard

menu_router = Router()


@menu_router.message(commands=["start"], state='*')
async def menu_handler(message: Message, state: FSMContext):
    await message.answer(text="\n".join([f"Добро пожаловать"]),
                         reply_markup=main_menu_keyboard(is_admin=False))


@menu_router.callback_query(GoToCb.filter(F.action == 'menu'), state='*')
async def go_to_menu_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text="\n".join([f"Добро пожаловать"]),
                                 reply_markup=main_menu_keyboard(is_admin=False))
