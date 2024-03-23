from aiogram import Dispatcher, Bot

import asyncio

from handlers.admin_bot_handlers import admin_router
from settings import token_admin_bot, storage_admin_bot


async def main():
    bot = Bot(token=token_admin_bot, parse_mode="html")
    print(await bot.get_me())
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=storage_admin_bot)
    dp.include_routers(admin_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())