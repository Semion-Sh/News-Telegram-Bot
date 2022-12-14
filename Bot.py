from create_bot import dp, bot
from aiogram.utils import executor
# from Handlers import Client, Other, Admin, News
# from Handlers import News
import asyncio
# from Handlers.Other import spam_start, english_spam_start
# from DateBase import DATABASE
import os
from Handlers.News import start_news_ru
from Handlers.Waiters import start_waiters_ru
import tracemalloc


async def start_bot(_):
    asyncio.create_task(start_news_ru())
    asyncio.create_task(start_waiters_ru())
    # asyncio.create_task(news_by_meduza_war())
    # asyncio.create_task(news_by_bbc_russian())


# News.register_handlers_news(dp)
# Client.register_handlers_client(dp)
# Other.register_handlers_other(dp)
# Admin.register_handlers_admin(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
