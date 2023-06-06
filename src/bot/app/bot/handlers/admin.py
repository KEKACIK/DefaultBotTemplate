from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile

from app.bot.handlers.callbackdata import StartCb, AdminCb, GoToCb
from app.bot.handlers.keyboards.admin import admin_menu_keyboard
from app.core.constants import DATE_FORMAT, get_files_dir
from app.utils.excel.export import get_excel_user

admin_router = Router()


@admin_router.callback_query(StartCb.filter(F.action == 'admin'))
async def admin_menu_handler(call: CallbackQuery, state: FSMContext, _):
    await call.message.delete()
    await call.message.answer(text=_("messages.admin"), reply_markup=admin_menu_keyboard(_))


@admin_router.callback_query(AdminCb.filter(F.action == 'export_users'))
async def admin_export_handler(call: CallbackQuery, state: FSMContext, _):
    if await get_excel_user():
        date = datetime.now().strftime(DATE_FORMAT)
        print(f"{get_files_dir()}/USERS_{date}.xlsx")
        await call.message.answer_document(document=FSInputFile(f"{get_files_dir()}/USERS_{date}.xlsx"))
    else:
        print("ОШИБКА ВЫГРУЗКИ ФАЙЛА")
    await admin_menu_handler(call, state, _)


@admin_router.callback_query(GoToCb.filter(F.action == 'admin'))
async def go_to_admin_handler(call: CallbackQuery, state: FSMContext, _):
    await admin_menu_handler(call, state, _)
