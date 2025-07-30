import asyncio

from bot.bot_utils import register_middlewares, start_bot, stop_bot
from bot.config import bot, dp
from bot.users.router import user_router


async def main():
    # Регистрация middleware и роутеров
    await register_middlewares(dp)  # Используем функцию для регистрации middleware
    dp.include_router(user_router)

    # Регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # Запуск бота в режиме long polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
