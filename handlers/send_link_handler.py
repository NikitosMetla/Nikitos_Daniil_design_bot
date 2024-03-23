from aiogram import Router, Bot, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state

from data.data_base import Users
from data.keyboards import start_keyboard
from settings import send_link_photo_id
from utils.is_subscriber import is_subscriber

send_link_router = Router()


@send_link_router.callback_query(Text(startswith="start_send_link|"), any_state)
@is_subscriber
async def user_send_link(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    delete_message_id = int(message.data.split("|")[1])
    user = Users(message.from_user.id, "send_link_data")
    await user.read_data()  
    await user.add_user()
    link_website = '<a href="https://clc.to/slashstudy">ссылке</a>'
    link_base = '<a href="https://sly-gatsby-26a.notion.site/d89832d23afa42838fbb0250e4e94b72">ссылке</a>'
    await bot.delete_message(chat_id=message.from_user.id, message_id=delete_message_id)
    await message.message.answer_photo(caption=f"Получи самую большую базу знаний"
                                               f" по дизайну от студии Слеш по {link_base}💯",
                                       photo=send_link_photo_id)
    await message.message.answer(text=f"👉А еще больше полезного контента ты найдешь, перейдя по {link_website} на наш сайт")
    next_message = await message.message.answer("Выбирай, чего желаешь: узнать свою ЗП по рынку, крутануть"
                                               " рулетку на определения скиллов"
                                               " в дизайне, забрать самую большую базу по дизайну"
                                               " или получить личного ментора из топовой"
                                               " компании!")
    await next_message.edit_reply_markup(reply_markup=start_keyboard(next_message.message_id).as_markup())


# @send_link_router.message(F.text, any_state)
# @is_subscriber
# async def user_send_link(message: types.Message, state: FSMContext, bot: Bot):
#     await message.delete()
#     link_website = '<a href="https://clc.to/mento_1">ссылке</a>'
#     link_base = '<a href="https://sly-gatsby-26a.notion.site/d89832d23afa42838fbb0250e4e94b72">ссылке</a>'
#     await message.answer(text=f"Получи самую большую базу знаний по дизайну от студии Вайт по {link_base}💯")
#     await message.answer(text=f"👉А еще больше полезного контента ты найдешь, перейдя по {link_website} на наш сайт")