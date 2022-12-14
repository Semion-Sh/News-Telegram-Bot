from create_bot import bot, dp
from Config import *
from Keyboards.Errors_kb import inline_error_kb
from aiogram import types


async def send_error(link):
    await bot.send_message(chat_id='785933034',
                           text=f'''❗️Error to parse❗
{link}''',
                           reply_markup=inline_error_kb,
                           disable_web_page_preview=True,
                           parse_mode='html'
                           )


@dp.callback_query_handler(lambda x: x.data == 'corrected')
async def correct_error(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)