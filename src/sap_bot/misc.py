import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor

from .config import (LOGFILE, BOT_TOKEN, SKIP_UPDATES)

logging.basicConfig(level=logging.INFO, filename=LOGFILE)
loop = asyncio.get_event_loop()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
executor = Executor(dp, skip_updates=SKIP_UPDATES)



