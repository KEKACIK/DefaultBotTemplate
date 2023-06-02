import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from app.core.config import settings

app_dir: Path = Path(os.getcwd())
bot = Bot(settings.TELEGRAM_BOT_TOKEN, parse_mode="HTML")
storage = RedisStorage(redis=Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB))
dp = Dispatcher(storage=storage)
