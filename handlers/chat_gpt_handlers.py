import asyncio
import io
import random

from aiogram import Router, Bot, types, F
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.data_base import Users
from settings import design_questions, InputMessage, text_rofl, text_objective
from utils.is_subscriber import is_subscriber
from utils.rating_chat_gpt import RatingChatGpt

chat_gpt_router = Router()


@chat_gpt_router.callback_query(Text(startswith="ai_recommendation|"), any_state)
@chat_gpt_router.callback_query(Text(startswith="rofl_recommendation|"), any_state)
@is_subscriber
async def user_start_objective(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    delete_message_id = int(message.data.split("|")[1])
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вернуться в стартовое меню", callback_data="start_menu"))
    if "rofl_recommendation|" in message.data:
        attempts = True
        if attempts:
            await message.message.answer(text_rofl,reply_markup=keyboard.as_markup())
            await state.set_state(InputMessage.rofl_ai_recommendation_state)
            await state.update_data(rofl=True)
        else:
            keyboard = InlineKeyboardBuilder()
            keyboard.row(InlineKeyboardButton(text="Оплатить", url="sadfasdf"))
            keyboard.row(InlineKeyboardButton(text="В стартовое меню", callback_data="start_menu"))
            await message.message.answer('Для использования функции "Нейрокритик" нужно приобрести пакет из'
                                         ' 10 отзывов за 250 рублей.')
    else:
        await message.message.answer(text_objective, reply_markup=keyboard.as_markup())
        user = Users(message.from_user.id, "ai_recommendations")
        await user.read_data()
        await user.add_user()
        await state.set_state(InputMessage.objective_ai_recommendation_state)
        await state.update_data(rofl=False)
    # await users_repository.add_user(user_id=message.from_user.id, username=message.from_user.username)
    await bot.delete_message(chat_id=message.from_user.id, message_id=delete_message_id)


# @chat_gpt_router.callback_query(Text(text="pay_attempts"), any_state)
# @is_subscriber
# async def pay_attempts_bot(message: types.CallbackQuery, state: FSMContext, bot: Bot):
#     url = ""
#     await message.message.answer(f"Отлично, высылаем тебе ссылку для оплаты:\n\n{url}")


@chat_gpt_router.callback_query(Text(text="next_rofl_recommendation"), any_state)
@chat_gpt_router.callback_query(Text(text="next_objective_recommendation"), any_state)
@is_subscriber
async def user_new_photo(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    if message.data == "next_rofl_recommendation":
        await state.set_state(InputMessage.rofl_ai_recommendation_state)
        await state.update_data(rofl=True)
    else:
        await state.set_state(InputMessage.objective_ai_recommendation_state)
        await state.update_data(rofl=False)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вернуться в стартовое меню", callback_data="start_menu"))
    delete_message = await message.message.answer("Ожидаю от тебя картинку)", reply_markup=keyboard.as_markup())
    await state.update_data(delete_message_id=delete_message.message_id)
    await message.message.delete()


@chat_gpt_router.message(F.photo, InputMessage.rofl_ai_recommendation_state)
@chat_gpt_router.message(F.photo, InputMessage.objective_ai_recommendation_state)
@is_subscriber
async def get_photo_objective(message: types.Message, state: FSMContext, bot: Bot):
    rofl = await state.get_data()
    rofl, delete_message = rofl.get("rofl"), rofl.get("delete_message_id")
    if delete_message is not None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=delete_message)
    delete_message = await message.answer("Приняли твой дизайн 🎨. Нужно немного времени ⏳, чтобы проанализировать"
                                          " и дать ответ.")
    await state.clear()
    photo_bytes_io = io.BytesIO()
    await bot.download(message.photo[-1], destination=photo_bytes_io)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Вернуться в стартовое меню", callback_data="start_menu"))
    if rofl:
        answer_gpt = await RatingChatGpt(photo_bytes_io).assessment(False)
        text_after = ("Отлично! Если хочешь ещё больше мудрых советов, просто отправь ещё одну картинку 📸."
                      " Дай нашему Ai ещё один шанс разнести твой дизайн! 😄")
        keyboard.row(InlineKeyboardButton(text="Отправить еще одну картинку", callback_data="next_rofl_recommendation"))
    else:
        answer_gpt = await RatingChatGpt(photo_bytes_io).assessment(True)
        text_after = ("Отлично! Хочешь еще больше улучшений? Просто отправь еще одну картинку 📸, и наша Ai модель"
                      " подскажет, что можно сделать лучше. Давай вместе сделаем твой дизайн идеальным!")
        keyboard.row(InlineKeyboardButton(text="Отправить еще одну картинку",
                                          callback_data="next_objective_recommendation"))
    await delete_message.delete()
    await message.answer(text=answer_gpt)
    await asyncio.sleep(5)
    await message.answer(text_after, reply_markup=keyboard.as_markup())
