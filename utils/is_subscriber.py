import traceback
from functools import wraps

from aiogram.fsm.context import FSMContext

from aiogram import types, Bot

from settings import channel_id


def is_subscriber(func):
    @wraps(func)
    async def wrapper(message: types.Message | types.CallbackQuery, state: FSMContext, bot: Bot, **kwargs):
        # print("========================= " + func.__name__ + " ============================")
        try:
            chat_member = await bot.get_chat_member(channel_id, message.from_user.id)
            url = "https://t.me/slashstudy"
            link = '<a href="{}">канал</a>'.format(url)
            if chat_member.status in ["member", "administrator", "creator"]:
                # print('Проверка на подписку пройдена')
                return await func(message, state, bot, **kwargs)
            elif type(message) == types.Message:
                await message.delete()
                await message.answer(f"Дорогой друг, прежде чем воспользоваться нашим ботом тебе"
                                     f" нужно подписаться на {link}🔔")
            else:
                await message.message.answer(f"Дорогой друг, прежде чем воспользоваться нашим ботом"
                                             f" тебе нужно подписаться на {link}🔔")
        except Exception:
            print(traceback.format_exc())
        # finally:
        #     print("========================= " + func.__name__ + " ============================")

    return wrapper
