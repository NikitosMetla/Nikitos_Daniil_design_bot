import asyncio

from aiogram import Router, types, Bot, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot import design_bot
from data.admins import Admin
from data.data_base import Users
from data.keyboards import admin_keyboard, add_delete_admin, cancel_keyboard, choice_bot_stat, \
    back_to_bots_keyboard
from settings import InputMessage
from utils.is_main_admin import is_main_admin
from utils.list_admins_keyboard import Admins_kb

admin_router = Router()


@admin_router.message(F.video_note, any_state)
@is_main_admin
async def admin_cancel(message: types.Message, state: FSMContext, bot: Bot):
    print(message.video_note.file_id)


@admin_router.message(F.photo, any_state)
@is_main_admin
async def admin_cancel(message: types.Message, state: FSMContext, bot: Bot):
    print(message.photo[-1].file_id)


@admin_router.callback_query(Text(text="cancel"), any_state)
@is_main_admin
async def admin_cancel(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await state.clear()
    await call.message.answer(text="Вы находитесь на стартовой панели, выберите свои дальнейшие действия", reply_markup=admin_keyboard)
    await call.message.delete()


@admin_router.callback_query(Text(text="back_to_bots"), InputMessage.statistic)
@is_main_admin
async def admin_cancel(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.edit_text(text="Выберите бота, о котором хотите посмотреть статистику📊",
                                 reply_markup=choice_bot_stat.as_markup())


@admin_router.callback_query(Text(text="back_to_bots"))
@is_main_admin
async def admin_cancel(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.edit_text(text="Выберите бота, через которого хотите сделать рассылку✉️",
                                 reply_markup=choice_bot_stat.as_markup())


@admin_router.message(Text(text="/start"), any_state)
@is_main_admin
async def admin_start(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    await message.delete()
    await message.answer(text="Это Админ бот для студии Вайт. С помощью него вы можете получать статистику по"
                              " пользователям, попавшим в воронку, а также делать"
                              " дополнительные рассылки по пользователям🤖", reply_markup=admin_keyboard)


@admin_router.message(Text(text="Статистика"))
@is_main_admin
async def choice_bot_for_stat(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    await state.set_state(InputMessage.statistic)
    await message.answer(text="Выберите бота, о котором хотите посмотреть статистику📊",
                         reply_markup=choice_bot_stat.as_markup())


@admin_router.callback_query(Text(startswith="mailing|"), InputMessage.statistic)
@is_main_admin
async def get_stat(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    filename = call.data.split("|")[1]
    user = Users(call.from_user.id, filename)
    await user.read_data()
    stat_day, stat_month = await user.get_day_statistic(), await user.get_month_statistic()
    stat_all = await user.get_all_statistic()
    if filename != "send_link_data" and filename != "mentor_stat":
        text_message = (f"Статистика за день: <b>{stat_day[0]}</b>, из которых <b>{stat_day[1]}</b> прошли опрос \n"
                        f"Статистика за месяц: <b>{stat_month[0]}</b>, из которых <b>{stat_month[1]}</b> прошли опрос\n"
                        f"Статистика за все время: <b>{stat_all[0]}</b>, из которых <b>{stat_all[1]}</b> прошли опрос")
    else:
        text_message = (f"Статистика за день: <b>{stat_day[0]}</b>\n"
                        f"Статистика за месяц: <b>{stat_month[0]}</b>\n"
                        f"Статистика за все время <b>{stat_all[0]}</b>")
    await call.message.edit_text(text=text_message,
                                 reply_markup=back_to_bots_keyboard.as_markup())


@admin_router.message(Text(text="Сделать рассылку"))
@is_main_admin
async def new_mailing(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    message = await message.answer(text="Напиши сообщение, которое разошлется пользователям", reply_markup=cancel_keyboard.as_markup())
    await state.set_state(InputMessage.enter_message_mailing)
    await state.update_data(message_id=message.message_id)


@admin_router.message(F.text, InputMessage.enter_message_mailing)
@is_main_admin
async def enter_message_mailing(message: types.Message, state: FSMContext, bot: Bot):
    # if filename == "all_bots":
    data = await state.get_data()
    message_id = data.get("message_id")
    user1, user2, user3 = (Users(message.from_user.id, "design_level"), Users(message.from_user.id,
                                                                              "earnings_level"),
                           Users(message.from_user.id, "send_link_data"))
    await user1.read_data(), await user2.read_data(), await user3.read_data()
    users1, users2, users3 = await user1.get_bot_users(), await user2.get_bot_users(), await user3.get_bot_users()
    users_set = list(set(users1) | set(users2) | set(users3))
    for user in users_set:
        try:
            await design_bot.send_message(chat_id=user, text=message.text)
        except:
            continue
    await message.answer(text="Ваша рассылка отправлена всем пользователям бота", reply_markup=admin_keyboard)
    await bot.delete_message(message_id=message_id, chat_id=message.from_user.id)
    await state.clear()


@admin_router.message(Text(text="Добавить / удалить админа"))
@is_main_admin
async def add_or_delete_admin(message: types.Message, state: FSMContext, bot: Bot):
    await state.clear()
    await message.answer(text="Выберите свои дальнейшие действия", reply_markup=add_delete_admin.as_markup())


@admin_router.callback_query(Text(text="add_admin"))
@is_main_admin
async def enter_new_admin_id(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.edit_text(text="Отлично, теперь введи telegram id нового админа! Учти,"
                                      " что у нового админа должен быть чат с данным ботом",
                                 reply_markup=cancel_keyboard.as_markup())
    await state.set_state(InputMessage.enter_admin_id)


@admin_router.callback_query(Text(text="delete_admin"))
@is_main_admin
async def delete_old_admin(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    keyboard = await Admins_kb().generate_list()
    await call.message.edit_text(text="Отлично, теперь выбери из представленных telegram id, который хочешь удалить",
                                 reply_markup=keyboard.as_markup())


@admin_router.callback_query(Text(startswith="admin|"))
@is_main_admin
async def actions_admin(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    admin_id = call.data.split("|")[1]
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Удалить админа", callback_data=f"delete|{admin_id}"))
    keyboard.row(InlineKeyboardButton(text="Отмена", callback_data=f"cancel"))
    await call.message.edit_text(text="Выбери свои дальнейшие действия с админом!",
                                 reply_markup=keyboard.as_markup())


@admin_router.callback_query(Text(startswith="delete|"))
@is_main_admin
async def choice_delete_admin(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    admin_id = call.data.split("|")[1]
    await Admin(admin_id).delete_admin()
    await call.message.answer(text=f"Отлично, вы удалили аднима с telegram id {admin_id},"
                                   f" выберите свои дальнейшие действия!", reply_markup=admin_keyboard)
    await call.message.delete()


@admin_router.message(F.text, InputMessage.enter_admin_id)
@is_main_admin
async def add_mew_admin(message: types.Message, state: FSMContext, bot: Bot):
    try:
        await bot.send_message(chat_id=message.text, text="Вас добавили в данного бота, как админа!")
        await message.answer(text="Отлично, вы успешно добавили нового админа!", reply_markup=admin_keyboard)
        await message.delete()
        await Admin(message.text).add_admin()
        await state.clear()
    except:
        await message.answer(text="Данного telegram id не существует или у нового админа нет чата с ботом, убедитесь"
                                  " в корректности данных и попробуйте снова!",
                             reply_markup=cancel_keyboard.as_markup())
