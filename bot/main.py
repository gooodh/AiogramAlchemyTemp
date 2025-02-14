import asyncio
import tracemalloc
from aiohttp import web
from loguru import logger
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from config import BASE_URL, HOST, PORT, WEBHOOK_PATH, bot, dp
from users.router import user_router
from bot_utils import start_bot, stop_bot, register_middlewares


async def main():
    tracemalloc.start()

    # Регистрация middleware и роутеров
    register_middlewares(dp)  # Используем функцию для регистрации middleware
    dp.include_router(user_router)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    # Установка вебхука и логирование результата
    try:
        response = await bot.set_webhook(f"{BASE_URL}{WEBHOOK_PATH}")
        if response:
            logger.info(f"Вебхук успешно установлен: {response}.")
        else:
            logger.warning("Вебхук не установлен, ответ пуст.")
    except Exception as e:
        logger.error(f"Ошибка при установке вебхука: {e}")

    # Запускаем веб-сервер
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=HOST, port=PORT)
    await site.start()

    try:
        await start_bot()
        while True:
            await asyncio.sleep(3600)  # Ждем 1 час
    except KeyboardInterrupt:
        pass
    finally:
        await stop_bot()
        await runner.cleanup()
        logger.info("Ресурсы очищены.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Программа завершена пользователем.")
