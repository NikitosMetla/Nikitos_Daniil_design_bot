import os

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

channel_id = ""
storage_bot = MemoryStorage()
storage_admin_bot = MemoryStorage()

design_level_video_note2 = ""
mentor_video_note = ""

start_photo_id=""
design_level_photo_id=""
earnings_level_photo_id=""
send_link_photo_id=""

senior_photo_id=""
middle_photo_id=""
junior_photo_id=""
artdir_photo_id=""
interesant_photo_id=""

token_design_level = ""

token_admin_bot = ""

class InputMessage(StatesGroup):
    design_level = State()
    earning_level = State()
    enter_admin_id = State()
    enter_message_mailing = State()
    statistic = State()


import random

design_questions = {
    "1 вопрос": {
        "content": "Проснулся, умылся, потянулся, что ты видишь перед собой❓",
        "answers": {
            "Таблички богу таблиц! Циферку трону циферок!": 4,
            "Монитор с фигмой, протопаем и всеми этими дизайнерскими штуками": 3,
            "Поисковики, ссылки на эти ваши дизигнерские каналы и ютубчики": 1,
            "Лоток": 0,
        }
    },
    "2 вопрос": {
        "content": "Как ты выстраиваешь свой распорядок дня и работу❓",
        "answers": {
            "Захожу в родненький битрикс и смотрю, что мне намурчали на день": 3,
            "Не приступаю, пока не отпишу своего лиду и у него не уточню «Что делать?»": 2,
            "Интуитивно. Никогда ничего не трекаю": 1,
            "Веду задачи как в корпоративном таск-менеджере, так и для себя все отмечаю в ноушене": 4,
        }
    },
    "3 вопрос": {
        "content": "А за сколько времени ты можешь уложиться в задачку❓",
        "answers": {
            "Отправлю задачи своим дизайнерам, пусть разбираются сами": 3,
            "Пойду к лиду и уточню сроки, буду опираться на них": 2,
            "Очень шустро, примерно на час… Я не знаю)": 0,
            "На каждую свою задачу, примерно знаю сколько уходит) Наверное": 1,
        }
    },
    "4 вопрос": {
        "content": "К тебе пришла знакомая в личку, сказала, что есть выходы на интересные проекты."
                   " Как ты максимально ёмко расскажешь, насколько ты крут(а) в этом❓",
        "answers": {
            "Я делал слишком многое, чтобы бояться любых, даже самых сложных проектов": 2,
            "Мои дизайнеры и не такое сварганят": 3,
            "А чо там делать надо? Я и не такое с гуглом и молитвами делал!": 1,
            "Я не смогу взяться, так как сложно… Всего хорошего!)": 0,
        }
    },
    "5 вопрос": {
        "content": "Друже, а ты с граф.дизайном дружишь? А можешь в коммуникацию? Баннеры, соц.сетки, лэндосы❓",
        "answers": {
            "Делал для продукта кое-что, надо же было интерфейски разукрасить": 2,
            "Делал постеры для корешей на пятничный FLEXXX": 1,
            "Мои ребятки сделают для вас ЭПОЛ на максималке": 3,
            "Да я, а ты?": 0,
        }
    },
    "6 вопрос": {
        "content": "Твоя любимая шаверма решила ребрендиться. Твой друг Ашот предложил тебе разобраться с этим. Что ты ответишь❓",
        "answers": {
            "Сделаю со своими ребятами «чисто по приколу»": 3,
            "Бесплатно кормить будешь? Тогда сделаю (Как смогу)": 0,
            "Уломаю лида пойти со мной делать за бесплатную шавуху": 1,
            "За мой фирстиль парень обанкротится)": 2,
        }
    },
    "7 вопрос": {
        "content": "Как ты проводишь свободное время на работе❓ (Если у тебя такое бывает…)",
        "answers": {
            "Сделаю гайды для команды, чтобы масштабироваться в дальнейшем грядущем": 3,
            "Пройдусь по задачкам, посмотрю, как ускорить свой рабочий процесс": 2,
            "Пройдусь по своим референсам, сделаю шотик для дрибла": 1,
            "Лягу на бочёк, поурчу… Посплю)": 0,
        }
    },
    "8 вопрос": {
        "content": "Твоя команда взяла новый продукт. Надо побрейнштормить! Чем будешь заниматься❓",
        "answers": {
            "Запишу все лучшие идеики и замутим новый проект": 3,
            "Будем обсуждать каждый инсайт и запишем ВСЁ!": 2,
            "Я выскажу им все! Пусть слушают!!!": 1,
            "Хочу послушать ребят, не буду ничего говорить, чтобы не показаться глупеньким": 0,
        }
    },
    "9 вопрос": {
        "content": "На твои идейки пара человек сказали «посиди тихо, не урчи!» Твои действия❓",
        "answers": {
            "Они сказали, я сказал. Надо потестить все версии": 3,
            "Сейчас я разберу по частям вами сказанное! Складывается впечатление, что у каждого свои взгляды": 2,
            "Это ваше мнение, оставьте его при себе!)": 1,
            "Сейчас вы у меня спать ляжете!!!!": 0,
        }
    },
    "10 вопрос": {
        "content": "Ты смотришь на часы. Настал конец рабочего дня. Чем дома займешься❓",
        "answers": {
            "Подведу итоги дня. Запишу задачки на завтра и отбой!": 2,
            "Конец дня? Я работаю всегда, жернова крутятся, работа мутится, продукт растёт!!!!": 3,
            "Доделаю задачи, которые оставил недобитыми": 1,
            "Посмотрю сериальчик": 0,
        }
    },
}


earnings_questions = {
    "1 вопрос": {
        "content": "Так, подрубаем с тобой созвон! Вкратце, кто ты❓",
        "answers": {
            "Хаюшки, я граф-диз, делаю красоту для брендов. Отрисовываю лого, делаю упаковки, короче, полную коммуникацию брендов)": 1,
            "Сау, я интерфейсник. Делаю ui/ux этот ваш) Веб, приложухи… Довожу людей от первого клика до покупки внутри продукта)": 2,
            "Привет! Я делаю картинку живой) Шарю в моушене, делаю контент для инсты и юпуп блогеров. Мои работы возможно ты видел в трендах)": 3,
            "Доброго времени суток! Я продуктовый дизайнер, проникаю в душу пользователей исследованиями, тестами и выискиваю боли каждого, прокачивая их": 4,
        }
    },
    "2 вопрос": {
        "content": "В каких прогах ты делаешь свою красоту❓",
        "answers": {
            "В Adobe Photoshop, Illustrator, Corel Draw или Adobe Indesign. Могу и в Figma что-то поковырять)": 1,
            "Figma, Sketch, InVision, Axure": 2,
            "В основном зависаю в Blender 3D или Cinema 4D, Zbrush, Houdini, Unity или Unreal Engine": 3,
            "Чаще всего работаю в Adobe After Effects или Cinema 4D, Adobe Premier Pro, Unity": 4,
        }
    },
    "3 вопрос": {
        "content": "Сколько ты в профессии❓",
        "answers": {
            "Почти год": 1,
            "Скоро 3 года": 2,
            "Почти 5 лет": 3,
            "Больше 7ми лет": 4,
        }
    },
    "4 вопрос": {
        "content": "А где работал❓",
        "answers": {
            "Пока нигде": 1,
            "В 1ом продукте": 2,
            "Несколько студий, сейчас сижу в продукте": 3,
            "Слишком много где был, не перечесть)": 4,
        }
    },
    "5 вопрос": {
        "content": "А кто ты по грейду❓",
        "answers": {
            "Джун работящий": 1,
            "Мидл рассуждающий": 2,
            "Сеньор высокопоставляющий": 3,
            "Арт-дир созидающий": 4,
        }
    },
    "6 вопрос": {
        "content": "Как работать любишь❓",
        "answers": {
            "Еще никак": 1,
            "Беру проекты, но работаю в основном продукте": 2,
            "Сижу в штате": 3,
            "Работаю внутри большой компании, в своей студии": 4,
        }
    },
    "7 вопрос": {
        "content": "Людьми управлял когда-нибудь❓",
        "answers": {
            "Не-а": 1,
            "Было такое": 2,
            "От 3 до 6": 3,
            "До 15 и больше": 4,
        }
    },
    "8 вопрос": {
        "content": "Что по портфолио❓",
        "answers": {
            "К сожалению, его нет(": 1,
            "Несколько реальных проектов, остальные для массовки, скилл показывать)": 2,
            "Достаточно много проектов и продуктов": 3,
            "Я сам путаюсь в этом архиве…Думаю, за месяц разгрести можно) Закину ссылочку)": 4,
        }
    },
    "9 вопрос": {
        "content": "Сейчас учишься где❓",
        "answers": {
            "Ютубчик, инста, какие-то советы от коллег": 1,
            "Курс параллельно работе прохожу": 2,
            "Менторы, консультации и много-много чего": 3,
            "Я слишком много знаю. Запиши мои онбординги джунам – можно курс продавать)": 4,
        }
    },
    "10 вопрос": {
        "content": "Чо по бабкам хочешь? А сколько получал❓",
        "answers": {
            "30к было, разок…": 1,
            "До 60к доходило за месяц": 2,
            "Сотка, может 120к было": 3,
            "Двух чемоданов, чтобы сложить не хватит)": 4,
        }
    },
}


user_levels = {
    "Стремящийся интересант": [0, 10],
    "Джун работящий": [11, 15],
    "Мидл рассуждающий": [16, 20],
    "Сеньор высокопоставляющий": [21, 28],
    "Арт-дир созидающий": [29, 40]
}

level_photos = {
    "Джун работящий": junior_photo_id,
    "Мидл рассуждающий": middle_photo_id,
    "Сеньор высокопоставляющий": senior_photo_id,
    "Арт-дир созидающий": artdir_photo_id,
    "Стремящийся интересант": interesant_photo_id
}

user_earning = {
    "30000 ₽": [0, 10],
    "60000 ₽": [11, 15],
    "80000 ₽": [16, 20],
    "120000 ₽": [21, 28],
    "200000 ₽": [29, 40]
}

user_earning_photos = {
    "30000 ₽": interesant_photo_id,
    "60000 ₽": junior_photo_id,
    "80000 ₽": middle_photo_id,
    "120000 ₽": senior_photo_id,
    "200000 ₽": artdir_photo_id,
}

options = ["Точно первый", "Скорее второй", "Третий, однозначно", "Четвертый, базарю"]

stickers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
