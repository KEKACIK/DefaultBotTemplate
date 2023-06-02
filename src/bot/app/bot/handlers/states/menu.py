from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    login = State()
    password = State()
    submit = State()
