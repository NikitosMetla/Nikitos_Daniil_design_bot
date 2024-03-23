from aiogram import Router, Bot, types, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state

from data.data_base import Users
from data.keyboards import start_keyboard
from settings import send_link_photo_id, mentor_video_note
from utils.is_subscriber import is_subscriber

mentor_router = Router()


@mentor_router.callback_query(Text(startswith="mentor|"), any_state)
@is_subscriber
async def user_send_mentor(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    user = Users(message.from_user.id, "mentor_stat")
    await user.read_data()
    await user.add_user()
    await message.message.answer_video_note(video_note=mentor_video_note)
    link = '<a href="https://t.me/slashstudy">Слеш</a>'
    await message.message.answer(f'Этот бот создан ребятами из Слеш.\n\n{link} - это твой старший брат в дизайне. Ментор, задача которого реально помочь тебе стать круче. При этом не задолбать пушами и сухими ответами, а как настоящий друг: быть рядом, направлять на верный путь и поддерживать во время дороги.\n\nСеньор и лид дизайнеры из Ozon, Yandex, СБЕР, МТС и других крупных компаний копнут в твои проблемы/хотелки и составят личный план развития в ноушене. По ходу пути все время будут с тобой отвечая на любые  вопросы, начиная от "Как создать компонент в фигме" заканчивая "Как забрать тендер с корпорацией".')
    await message.message.answer("Забирай звонок с топом по скидке 30% до 20 апреля: slashstudy.ru")
    next_message = await message.message.answer("Выбирай, чего желаешь: узнать свою ЗП по рынку, крутануть"
                                             " рулетку на определения скиллов"
                                             " в дизайне, забрать самую большую базу по дизайну"
                                             " или получить личного ментора из топовой"
                                             " компании!")
    await next_message.edit_reply_markup(reply_markup=start_keyboard(next_message.message_id).as_markup())