from loguru import logger
import aiogram
logger.info(aiogram.__version__)
from app import misc
from app.bot.handlers import menu_router
from db.init_db import init_db
from utils.logger import configure_logger


def setup():
    import app.bot.middlewares.big_bro # noqa
    misc.dp.include_router(menu_router)


async def on_startup():
    configure_logger(True)

    try:
        await init_db()
    except ConnectionRefusedError:
        logger.error("Failed to connect to database ")
        exit(1)

    setup()
    logger.info("Success init")


if __name__ == '__main__':
    misc.dp.startup.register(on_startup)
    misc.dp.run_polling(misc.bot)
