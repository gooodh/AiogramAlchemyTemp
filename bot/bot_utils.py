from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger
from bot.config import bot, admins

from bot.dao.database_middleware import (
    DatabaseMiddlewareWithCommit,
    DatabaseMiddlewareWithoutCommit,
)


async def register_middlewares(dp):
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())


async def set_commands():
    commands = [BotCommand(command="start", description="Старт")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def notify_admins(message):
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, message)
        except Exception as e:
            logger.error(
                f"Ошибка при отправке сообщения администратору {admin_id}: {e}"
            )


async def start_bot():

    await set_commands()
    await notify_admins("Я запущен🥳.")
    logger.info("Бот успешно запущен.")


async def stop_bot():
    await notify_admins("Бот остановлен. За что?😔")
    logger.error("Бот остановлен!")
