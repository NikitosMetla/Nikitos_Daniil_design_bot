import os

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

channel_id = "-1001737287489"
storage_bot = MemoryStorage()
storage_admin_bot = MemoryStorage()

design_level_video_note1 = "DQACAgIAAxkBAAIBcWX_F-Nj6cZg8xHnMHLRJkC-cbbNAAJ1QgACBdbRSO2Krjvatf-xNAQ"
design_level_video_note2 = "DQACAgIAAxkBAAICEWX_L1V11WePro9SGsCi5vGRtH9eAAKjSgACR2KwS8f-6qb3GnwoNAQ"
mentor_video_note = "DQACAgIAAxkBAAICwGX_NLyTRzpmIMYpqnEEK0mhZDatAAJgRAACNMzpS3NMAAFO6bI2mTQE"


earnings_level_video_note1 = ""
earnings_level_video_note2 = ""

start_photo_id="AgACAgIAAxkBAAONZeyyHF_5AmzNgvbA0h0XKuH_NQgAA9oxG4U1YEsm9vS-hp3P4AEAAwIAA3kAAzQE"
design_level_photo_id="AgACAgIAAxkBAAOaZey0f12CWsfpUiowWdjnEIA2R8UAAizaMRuFNWBLlpICXeTFXUgBAAMCAAN5AAM0BA"
earnings_level_photo_id="AgACAgIAAxkBAAOZZey0cOeTtWHaQQtdGxqC0lAkqHYAAifaMRuFNWBLLrWDvu28zEoBAAMCAAN5AAM0BA"
send_link_photo_id="AgACAgIAAxkBAAOYZey0W6GKz7os4XhzYpINwsZEtfMAAiXaMRuFNWBLpzZFf_uTA4EBAAMCAAN5AAM0BA"

senior_photo_id="AgACAgIAAxkBAAOVZeyzq1JtuXJN629vdDUFVuuWo8QAAhjaMRuFNWBLzr1Vr7VUDbsBAAMCAAN5AAM0BA"
middle_photo_id="AgACAgIAAxkBAAOUZeyzoMKZFLgxfxyBzbftxaENLjYAAhfaMRuFNWBLYif8UlyrO9oBAAMCAAN5AAM0BA"
junior_photo_id="AgACAgIAAxkBAAOTZeyzV7Ra6mhsn_rWgtJZS4Q8EQwAAhPaMRuFNWBLPLaZrylQpuwBAAMCAAN5AAM0BA"
artdir_photo_id="AgACAgIAAxkBAAOXZey0Ba3aSIkgJ4x8pxpg7azZje4AAiLaMRuFNWBLMn381EbY_XABAAMCAAN5AAM0BA"
interesant_photo_id="AgACAgIAAxkBAAOWZeyzt79717tJwqoU7Q3ducWghPAAAhnaMRuFNWBLsKnjc8HoTiUBAAMCAAN5AAM0BA"

token_design_level = "6634629064:AAHAFVlb4UwS7NUUUIZG6ZVVEDb-7PC9TfY"

token_admin_bot = "6752520352:AAHUSSHHSr-PU5C4PWfWGsCXDOmkAXHKz_k"

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
            "Таблички богу таблиц! Циферку трону циферок!": 3,
            "Монитор с фигмой, протопаем и всеми этими дизайнерскими штуками": 2,
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
            "Хаюшки, я граф-диз, делаю красоту для брендов. Отрисовываю лого, делаю упаковки, короче, полную коммуникацию брендов)": 0,
            "Сау, я интерфейсник. Делаю ui/ux этот ваш) Веб, приложухи… Довожу людей от первого клика до покупки внутри продукта)": 1,
            "Привет! Я делаю картинку живой) Шарю в моушене, делаю контент для инсты и юпуп блогеров. Мои работы возможно ты видел в трендах)": 2,
            "Доброго времени суток! Я продуктовый дизайнер, проникаю в душу пользователей исследованиями, тестами и выискиваю боли каждого, прокачивая их": 3,
        }
    },
    "2 вопрос": {
        "content": "В каких прогах ты делаешь свою красоту❓",
        "answers": {
            "В Adobe Photoshop, Illustrator, Corel Draw или Adobe Indesign. Могу и в Figma что-то поковырять)": 0,
            "Figma, Sketch, InVision, Axure": 1,
            "В основном зависаю в Blender 3D или Cinema 4D, Zbrush, Houdini, Unity или Unreal Engine": 2,
            "Чаще всего работаю в Adobe After Effects или Cinema 4D, Adobe Premier Pro, Unity": 3,
        }
    },
    "3 вопрос": {
        "content": "Сколько ты в профессии❓",
        "answers": {
            "Почти год": 0,
            "Скоро 3 года": 1,
            "Почти 5 лет": 2,
            "Больше 7ми лет": 3,
        }
    },
    "4 вопрос": {
        "content": "А где работал❓",
        "answers": {
            "Пока нигде": 0,
            "В 1ом продукте": 1,
            "Несколько студий, сейчас сижу в продукте": 2,
            "Слишком много где был, не перечесть)": 3,
        }
    },
    "5 вопрос": {
        "content": "А кто ты по грейду❓",
        "answers": {
            "Джун работящий": 0,
            "Мидл рассуждающий": 1,
            "Сеньор высокопоставляющий": 2,
            "Арт-дир созидающий": 3,
        }
    },
    "6 вопрос": {
        "content": "Как работать любишь❓",
        "answers": {
            "Еще никак": 0,
            "Беру проекты, но работаю в основном продукте": 1,
            "Сижу в штате": 2,
            "Работаю внутри большой компании, в своей студии": 3,
        }
    },
    "7 вопрос": {
        "content": "Людьми управлял когда-нибудь❓",
        "answers": {
            "Не-а": 0,
            "Было такое": 1,
            "От 3 до 6": 2,
            "До 15 и больше": 3,
        }
    },
    "8 вопрос": {
        "content": "Что по портфолио❓",
        "answers": {
            "К сожалению, его нет(": 0,
            "Несколько реальных проектов, остальные для массовки, скилл показывать)": 1,
            "Достаточно много проектов и продуктов": 2,
            "Я сам путаюсь в этом архиве…Думаю, за месяц разгрести можно) Закину ссылочку)": 3,
        }
    },
    "9 вопрос": {
        "content": "Сейчас учишься где❓",
        "answers": {
            "Ютубчик, инста, какие-то советы от коллег": 0,
            "Курс параллельно работе прохожу": 1,
            "Менторы, консультации и много-много чего": 2,
            "Я слишком много знаю. Запиши мои онбординги джунам – можно курс продавать)": 3,
        }
    },
    "10 вопрос": {
        "content": "Чо по бабкам хочешь? А сколько получал❓",
        "answers": {
            "30к было, разок…": 0,
            "До 60к доходило за месяц": 1,
            "Сотка, может 120к было": 2,
            "Двух чемоданов, чтобы сложить не хватит)": 3,
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
    "30000 руб": [0, 10],
    "60000 руб": [11, 15],
    "80000 руб": [16, 20],
    "120000 руб": [21, 28],
    "200000 руб": [29, 40]
}

options = ["Точно первый", "Скорее второй", "Третий, однозначно", "Четвертый, базарю"]

stickers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]