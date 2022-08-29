from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from time import sleep
import json
from config import *
from scrapper import *
from helper_checker import checker
import requests

app = Client("Olga", api_hash=api_hash_4, api_id=api_id_4)

token = "5669125136:AAFztoGGP94HY7aPXqqxMtZWYCO6S5MaK54"
chat_id2 = ""
deal_link = ""
deal_link5 = ""
deal_links = []


@app.on_message(filters.command("start", prefixes="/"))
async def scrap_command(_, message: types.Message):
    chat_id2 = message.chat.id
    await app.send_message(chat_id2, "started")
    sleep(0.3)
    chat_id1 = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id1 = chat_id1.id
    await app.send_message(chat_id1, "🔎 Orderbook")
    sleep(1.5)


counter = 0


# .first scrapper without scrolling by pages
@app.on_message(filters.bot)
async def on_first_order_book_message(_, message: types.Message):
    global deal_link, counter, chat_id2, deal_links, deal_link5
    user_ids = [5509075943, 5567539582, 5565706619, 5317258228, 5490278675]
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    # check_json()
    text = str(message.text)
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    if text.startswith("#"):
        counter += 1
        print(counter)
        scrap(text, info["min"], info["percents"], info["max"])
        if counter == 100:
            counter = 0
            sleep(150)
            await app.send_message(chat_id, "🔎 Orderbook")
        else:
            deal = reader("result.json")
            if deal:
                deal_link = deal[-1]["link"]
                if deal_link not in info:
                    msg = f"""Номер ордера: {deal[-1]["#"]}\n
                                                      НА сколько код: {deal[-1]["min"]}\n
                                                      Наценка: {deal[-1]["percent"]}%\n
                                                      Пользователь: {deal[-1]["user"]}\n
                                                      Банк: {deal[-1]["bank"]}\n
                                                      Link: {deal[-1]["link"]}\n
                                                      К оплате: {deal[-1]["max"]}"""
                    data1 = {"chat_id": -1001793309978, "text": msg}
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data1)
                    try:
                        for i in user_ids:
                            data = {"chat_id": i, "text": f".deal  {deal_link}"}
                            url = f"https://api.telegram.org/bot{token}/sendMessage"
                            requests.post(url, data=data)
                        # monocat
                        with open("out_json.txt", "a", encoding="utf-8") as file:
                            file.write(deal_link)
                    except Exception:
                        await app.send_message(chat_id, "🔎 Orderbook")
                    finally:
                        sleep(60)
                        add_in_json("result.json", [])
                else:
                    add_in_json("result.json", [])
                    await app.send_message(chat_id, "🔎 Orderbook")
            sleep(1.5)

            await app.send_message(chat_id, "🔎 Orderbook")
    else:
        await app.send_message(chat_id, "🔎 Orderbook")


@app.on_edited_message(filters.bot)
async def edited(_, message: types.Message):
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    text = str(message.text)
    scrap(text, info["min"], info["percents"], info["max"])
    await message.click("Refresh")
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    await app.send_message(chat_id, "🔎 Orderbook")
    sleep(1.5)


@app.on_message(filters.command("stop", prefixes="."))
async def stop(_, message: types.Message):
    await message.reply("Я Остановился!")
    sleep(10)


@app.on_message(filters.command("hi", prefixes="."))
async def hi(_, msg: types.Message):
    await msg.reply("hello")


if __name__ == '__main__':
    app.run()
