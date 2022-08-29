from aiogram import Dispatcher, Bot, types, executor
import json
from scrapper import add_in_json

TOKEN = "5669125136:AAFztoGGP94HY7aPXqqxMtZWYCO6S5MaK54"
bot = Bot(token=TOKEN, parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands="p")
async def percent(message: types.Message):
    if message.chat.id == -1001793309978:
        percents = float(message.text.split("/p ", maxsplit=1)[1])
        with open("checker_db.json", "r", encoding="utf-8") as file:
            info = json.load(file)
        info["percents"] = percents
        with open("checker_db.json", "w", encoding="utf-8") as file:
            json.dump(info, file, indent=3)
        await message.answer(f"Min: {info['min']}\n"
                             f"\n"
                             f"Max: {info['max']}\n"
                             f"\n"
                             f"Наценка: {info['percents']}%")


@dp.message_handler(commands="min")
async def minimum(message: types.Message):
    if message.chat.id == -1001793309978:
        min_ = int(message.text.split("/min ", maxsplit=1)[1])
        with open("checker_db.json", "r", encoding="utf-8") as file:
            info = json.load(file)
        info["min"] = min_
        with open("checker_db.json", "w", encoding="utf-8") as file:
            json.dump(info, file, indent=3)
        await message.answer(f"Min: {info['min']}\n"
                             f"\n"
                             f"Max: {info['max']}\n"
                             f"\n"
                             f"Наценка: {info['percents']}%")


@dp.message_handler(commands="max")
async def maximum(message: types.Message):
    if message.chat.id == -1001793309978:
        max_ = int(message.text.split("/max ", maxsplit=1)[1])
        with open("checker_db.json", "r", encoding="utf-8") as file:
            info = json.load(file)
        info["max"] = max_
        with open("checker_db.json", "w", encoding="utf-8") as file:
            json.dump(info, file, indent=3)
        await message.answer(f"Min: {info['min']}\n"
                             f"\n"
                             f"Max: {info['max']}\n"
                             f"\n"
                             f"Наценка: {info['percents']}%")


@dp.message_handler(commands="clear")
async def clear(message: types.Message):
    if message.chat.id == -1001793309978:
        add_in_json("result.json", [])
        add_in_json("last_results.json", [])
        with open("out_json.txt", "w", encoding="utf-8") as file:
            file.write("")
        await message.answer("Все очищено!")


@dp.message_handler(commands="settings")
async def settings(message: types):
    if message.chat.id == -1001793309978:
        with open("checker_db.json", "r", encoding="utf-8") as file:
            text = json.load(file)
        await message.reply(f"Min: {text['min']}\n"
                            f"\n"
                            f"Max: {text['max']}\n"
                            f"\n"
                            f"Наценка: {text['percents']}%")


if __name__ == '__main__':
    executor.start_polling(dp)
