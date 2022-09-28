from aiogram import Bot, executor, types, Dispatcher
import re

bot = Bot(token="5474405893:AAEyFrMrs0DNRaXZQqYZAfdaKmKzVRnXGnY", parse_mode="HTML")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="deal")
async def deal(message: types.Message):
    print(message.text)


if __name__ == '__main__':
    print(re.findall("/deal", "jdsadnasd/deal"))
    executor.start_polling(dp, skip_updates=True)
