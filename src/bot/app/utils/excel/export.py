from datetime import datetime, timedelta
from io import BytesIO

from openpyxl.workbook import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from app import repo
from app.core.constants import get_files_dir, DATE_FORMAT
from app.utils.excel.base import reform


async def get_excel_user() -> bool:
    wb = Workbook()
    ws = wb.active
    users = await repo.users.get_all()
    ws.append(["ID", "Username", "Админ", "Язык", "Дата регистрации"])
    for user in users:
        ws.append([user.id, user.username, "Да" if user.is_admin else "Нет", user.locale, user.created_at])
    ws = reform(ws)
    date = datetime.now().strftime(DATE_FORMAT)
    wb.save(f"{get_files_dir()}/USERS_{date}.xlsx")
    return True
