from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.admins import Admin


class Admins_kb:
    async def generate_list(self):
        admins = await Admin().get_admins()
        keyboard = InlineKeyboardBuilder()
        for admin in admins:
            keyboard.row(InlineKeyboardButton(text=f"{admin}", callback_data=f"admin|{admin}"))
        keyboard.row(InlineKeyboardButton(text="Отмена", callback_data="cancel"))
        return keyboard