from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from time import sleep
import json
from config import *
from scrapper import *
from helper_checker import checker
import aiohttp

app = Client("19", api_hash=api_hash_19, api_id=api_id_19)

token = "5669125136:AAFztoGGP94HY7aPXqqxMtZWYCO6S5MaK54"
chat_id2 = ""
deal_link = ""
deal_link5 = ""
deal_links = []


@app.on_message(filters.command("start", prefixes="/"))
async def scrap_command(_, message: types.Message):
    chat_id2 = message.chat.id
    await app.send_message(chat_id2, "started")
    chat_id1 = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id1 = chat_id1.id
    await app.send_message(chat_id1, "🔎 Orderbook")
    sleep(1.5)


counter = 0


# .first scrapper without scrolling by pages
@app.on_message(filters.bot)
async def on_first_order_book_message(_, message: types.Message):
    global deal_link, counter, chat_id2, deal_links, deal_link5
    # user_ids = [5567539582, 5509075943, 5565706619, 5317258228, 5490278675]
    with open("checker_db.json", "r", encoding="utf-8") as file:
        info = json.load(file)
    text = str(message.text)
    chat_id = 786805975
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
                if deal_link:
                    try:
                        async with aiohttp.ClientSession() as session:
                            msg = f"Номер ордера: {deal[-1]['#']}\n" \
                                  f"НА сколько код: {deal[-1]['min']}\n" \
                                  f"Наценка: {deal[-1]['percent']}%\n" \
                                  f"Пользователь: {deal[-1]['user']}\n" \
                                  f"Банк: {deal[-1]['bank']}\n" \
                                  f"Link: {deal[-1]['link']}\n" \
                                  f"К оплате: {deal[-1]['max']}"
                            data1 = {"chat_id": -1001793309978, "text": msg}
                            await session.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data1)
                            data = {"chat_id": -1001687565244, "text": f"{deal_link}"}
                            url = f"https://api.telegram.org/bot{token}/sendMessage"
                            await session.post(url, data=data)
                            # with open("out_json.txt", "a", encoding="utf-8") as file:
                            #     file.write(deal_link)
                    except Exception:
                        await app.send_message(chat_id, "🔎 Orderbook")
                    finally:
                        sleep(5)
                        add_in_json("result.json", [])
                else:
                    add_in_json("result.json", [])
                    await app.send_message(chat_id, "🔎 Orderbook")
            sleep(1.5)
            await app.send_message(chat_id, "🔎 Orderbook")
    else:
        await app.send_message(chat_id, "🔎 Orderbook")



@app.on_message(filters.command("stop", prefixes="/"))
async def stop(_, message: types.Message):
    await message.reply("Я Остановился!")
    sleep(10)


@app.on_message(filters.command("hi", prefixes="."))
async def hi(_, msg: types.Message):
    await msg.reply("hello")


if __name__ == '__main__':
    app.run()
