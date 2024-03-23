from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

admin_kb = [
        [KeyboardButton(text='Статистика')],
        [KeyboardButton(text="Сделать рассылку")],
        [KeyboardButton(text="Добавить / удалить админа")]
    ]
admin_keyboard = ReplyKeyboardMarkup(keyboard=admin_kb, resize_keyboard=True)


def start_keyboard(message_id: int):
    start_keyboard = InlineKeyboardBuilder()
    start_keyboard.row(InlineKeyboardButton(text="Личный ментор (new!)", callback_data=f"mentor|{message_id}"))
    start_keyboard.row(InlineKeyboardButton(text="Скилл-детектор", callback_data=f"start_design_level|{message_id}"))
    start_keyboard.row(InlineKeyboardButton(text="ЗпСканнер", callback_data=f"start_earnings_level|{message_id}"))
    start_keyboard.row(InlineKeyboardButton(text="База знаний", callback_data=f"start_send_link|{message_id}"))
    return start_keyboard


add_delete_admin = InlineKeyboardBuilder()
add_delete_admin.row(InlineKeyboardButton(text="Добавить админа", callback_data="add_admin"))
add_delete_admin.row(InlineKeyboardButton(text="Удалить админа", callback_data="delete_admin"))

choice_bot_stat = InlineKeyboardBuilder()
choice_bot_stat.row(InlineKeyboardButton(text="Личный ментор", callback_data="mailing|mentor_stat"))
choice_bot_stat.row(InlineKeyboardButton(text="Уровень дизайна", callback_data="mailing|design_level"))
choice_bot_stat.row(InlineKeyboardButton(text="Уровень зароботка", callback_data="mailing|earnings_level"))
choice_bot_stat.row(InlineKeyboardButton(text="Отправитель методички", callback_data="mailing|send_link_data"))
choice_bot_stat.row(InlineKeyboardButton(text="Отмена", callback_data="cancel"))

choice_bot_send = InlineKeyboardBuilder()
choice_bot_send.row(InlineKeyboardButton(text="По всем ботам", callback_data="mailing|all_bots"))
choice_bot_send.row(InlineKeyboardButton(text="Уровень дизайна", callback_data="mailing|design_level"))
choice_bot_send.row(InlineKeyboardButton(text="Уровень зароботка", callback_data="mailing|earnings_level"))
choice_bot_send.row(InlineKeyboardButton(text="Отправитель методички", callback_data="mailing|send_link_data"))
choice_bot_send.row(InlineKeyboardButton(text="Отмена", callback_data="cancel"))

cancel_keyboard = InlineKeyboardBuilder()
cancel_keyboard.row(InlineKeyboardButton(text="Отмена", callback_data="cancel"))

back_to_bots_keyboard = InlineKeyboardBuilder()
back_to_bots_keyboard.row(InlineKeyboardButton(text="Назад к выбору ботов", callback_data="back_to_bots"))