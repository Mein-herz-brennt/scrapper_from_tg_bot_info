import time
from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from states import CardLimitChecker
from keyboards import *
import os
from my_parser import *

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    if message.from_user.id == 789402487 or 424079525:
        await message.answer("Привіт, що бажаєш вибрати?", reply_markup=menu_keyboard)


@dp.message_handler(text="Додати файл з картками")
async def add_file(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Надішліть будь ласка файл в форматі xlsx", reply_markup=back_keyboard)
    # await CardLimitChecker.file_with_cards.set()


@dp.message_handler(content_types="document")
async def read_and_send_info_about_file(message: types.Message, state: FSMContext):
    await state.finish()
    filename = message.document.file_name
    val = message.values
    if filename.endswith(".xlsx"):
        file_name = await message.document.download()
        print(file_name.name)
        await message.answer("Файл завантажено, перевірте коректність)")
        data = parse(file_name.name)
        for i in data:
            for key, item in i.items():
                if type(item) == list:
                    cards = card_string_generator(item)
                if key != "limit":
                    await message.answer(f"{key} - {i['limit']}\n"
                                         f"{cards}")
        await message.answer("Все вірно?", reply_markup=is_correct_keyboard)
    else:
        await message.answer("Надішліть будь ласка файл у вірному форматі, вірний формат - xlsx", reply_markup=back_keyboard)


@dp.message_handler(text="Назад", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ви повернулись в головне меню", reply_markup=menu_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
