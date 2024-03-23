import asyncio

from aiogram import Dispatcher, Bot
from handlers.design_level_handler import design_level_router
from handlers.earnings_level_handler import earnings_level_router
from handlers.mentor_handler import mentor_router
from handlers.send_link_handler import send_link_router
from settings import storage_bot, token_design_level

bot = Bot(token=token_design_level, parse_mode="html")


async def main():
    print(await bot.get_me())
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=storage_bot)
    dp.include_routers(mentor_router, design_level_router, earnings_level_router, send_link_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())