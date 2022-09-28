import requests as requests
from aiogram import Bot, Dispatcher, executor, types
import asyncio

bot = Bot(token="5683046357:AAHISAvJuPgJFKbzi8mXnm5BOr7Zyky6dfM", parse_mode="html")
dp = Dispatcher(bot=bot)

last_message1_in1_chat = ""


@dp.message_handler(content_types="text")
async def delete_identical_messages(message: types.Message):
    global last_message1_in1_chat
    if message.chat.id == -1001687565244:
        if last_message1_in1_chat == message.text:
            await bot.delete_message(-1001687565244, message.message_id)
        else:
            last_message1_in1_chat = message.text


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)