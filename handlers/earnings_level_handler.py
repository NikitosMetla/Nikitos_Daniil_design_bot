import random

from aiogram import Router, Bot, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.data_base import Users
from data.keyboards import start_keyboard
from settings import earnings_questions, InputMessage, options, stickers, earnings_level_photo_id, user_earning, \
    design_level_video_note1, design_level_video_note2
from utils.is_subscriber import is_subscriber

earnings_level_router = Router()


@earnings_level_router.callback_query(Text(startswith="start_earnings_level|"), any_state)
@is_subscriber
async def user_send_link(message: types.CallbackQuery, state: FSMContext, bot: Bot):
    delete_message_id = int(message.data.split("|")[1])
    user = Users(message.from_user.id, "earnings_level")
    await user.read_data()
    await user.add_user()
    keyboard = InlineKeyboardBuilder()
    question = earnings_questions.get('1 вопрос')
    for i, answer in enumerate(question.get("answers").keys()):
        keyboard.row(
            InlineKeyboardButton(text=options[i], callback_data=f"answer|{question.get('answers').get(answer)}|"
                                                                f"{1}"))
    answers = list(question.get("answers").keys())
    random.shuffle(answers)
    for i in range(len(answers)):
        answers[i] = f"{stickers[i]} {answers[i]}"
    text = (f"{1}."
            f" {question.get('content')}") + "\n    " + "\n    ".join(answers)
    await message.message.answer_photo(caption="Да начнется же тест «Сколько ты зарабатываешь?»! "
                                               "Ответь на десять вопросов и узнай, насколько ты богатый котик",
                                       photo=earnings_level_photo_id)
    await bot.delete_message(chat_id=message.from_user.id, message_id=delete_message_id)
    await message.message.answer(text=text, reply_markup=keyboard.as_markup())
    await state.set_state(InputMessage.earning_level)
    await state.update_data(last_question=1)


@earnings_level_router.callback_query(Text(startswith="answer|"), InputMessage.earning_level)
@is_subscriber
async def user_send_link(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = call.data.split("|")[1:]
    last_answer, last_question = int(data[0]), int(data[1])
    points = await state.get_data()
    if points.get("last_question") is None or (int(points.get("last_question")) != last_question):
        return
    points[str(last_question)] = last_answer
    points["last_question"] = last_question + 1
    await state.update_data(points)
    if last_question == 10:
        user = Users(call.from_user.id, "earnings_level")
        await user.read_data()
        await user.edit_completion()
        final_points = sum(points.values()) - int(points.get("last_question"))
        level = ""
        for key in user_earning.keys():
            if user_earning.get(key)[0] <= final_points <= user_earning.get(key)[1]:
                level = key
                break
        url = "https://clc.to/slashstudy"
        link_text = "сайте"
        link = '<a href="{}">{}</a>'.format(url, link_text)
        await call.message.answer(text=f"Спасибо за пройденный опрос. Ты можешь зарабатывать {level}🎊💪.\n"
                                       f"Еще больше полезного контента ты сможешь найти на нашем {link}🔚! Переходи быстрее"
                                       f", чтобы получить менторскую поддержку за самую вкусну цену.")
        # await bot.send_video_note(chat_id=call.from_user.id, video_note=earnings_level_video_note1)
        # await bot.send_video_note(chat_id=call.from_user.id, video_note=earnings_level_video_note2)
        next_message = await call.message.answer("Выбирай, чего желаешь: узнать свою ЗП по рынку, крутануть"
                                                  " рулетку на определения скиллов"
                                                  " в дизайне, забрать самую большую базу по дизайну"
                                                  " или получить личного ментора из топовой"
                                                  " компании!")
        await next_message.edit_reply_markup(reply_markup=start_keyboard(next_message.message_id).as_markup())
        await state.clear()
        return
    elif last_question == 5:
        await call.message.answer(text=f"Ты ответил на половину вопросов, поздравляем! Мы видим, что у тебя уже крутой уровень в дизайне, но как говорят великие – нет предела совершенству! Поэтому прокачивай свои скиллы в Слеш вместе с менторами из Ozon, Yandex, Сбер и других компаний, для этого забирай звонок с топом по скидке 30% до 20 апреля: slashstudy.ru")
        await bot.send_video_note(chat_id=call.from_user.id, video_note=design_level_video_note2)
    keyboard = InlineKeyboardBuilder()
    question = earnings_questions.get(f'{last_question + 1} вопрос')
    answers = list(question.get("answers").keys())
    random.shuffle(answers)
    for i, answer in enumerate(answers):
        keyboard.row(
            InlineKeyboardButton(text=options[i], callback_data=f"answer|{question.get('answers').get(answer)}|"
                                                                f"{last_question + 1}"))
    for i in range(len(answers)):
        answers[i] = f"{stickers[i]} {answers[i]}"
    text = (f"{last_question + 1}."
            f" {question.get('content')}") + "\n    " + "\n    ".join(answers)
    await call.message.answer(text=text,
                              reply_markup=keyboard.as_markup())
