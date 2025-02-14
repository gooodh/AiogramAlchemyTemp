import asyncio

from bot_utils import register_middlewares, start_bot, stop_bot
from config import bot, dp
from users.router import user_router


async def main():
    # Регистрация middleware и роутеров
    register_middlewares(dp)  # Используем функцию для регистрации middleware
    dp.include_router(user_router)

    # Регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # Запуск бота в режиме long polling
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
