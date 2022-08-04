from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from time import sleep
import json
from config import *
import aioschedule as schedule
from scrapper import *

app = Client("me", api_hash=api_hash_v, api_id=api_id_v)

chat_id1 = ""


# def job(_, message: types.Message):
#     message.click("Refresh")
#     print(1)


#
@app.on_message(filters.command("scrap", prefixes=".") & filters.me)
async def scrap_command(_, message: types.Message):
    global chat_id1
    chat_id = message.chat.id
    await app.send_message(chat_id, "started")
    chat_id1 = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id1 = chat_id1.id
    await app.send_message(chat_id1, "🔎 Orderbook")
    sleep(1.5)


# .first scrapper without scrolling by pages
@app.on_message(filters.bot)
async def on_first_order_book_message(_, message: types.Message):
    text = str(message.text)
    # print(text)
    scrap(text, 10, 0.5, 10000)
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    with open("out_json.txt", "r", encoding="utf-8") as file:
        text = file.read()
    if text == "True":
        i = reader("head_db.json")[-1]
        msg = f"""Order: {i["#"]}\n
                  Prise: {i["min"]} | {i["max"]}\n
                  Percents: {i["percent"]}%\n
                  User: {i["user"]}\n
                  Bank: {i["bank"]}\n
                  Link: {i["link"]}\n
                  Card: <code>{i["card"]}</code>"""
        await app.send_message(filters.me, msg)
    # await message.click("Refresh")
    await app.send_message(789402487, "🔎 Orderbook")
    sleep(3)

    # schedule.every().second.do(await message.click("Refresh"))
    # while True:
    #     schedule.run_pending()
    #     await asyncio.sleep(3)do(job)
    # schedule.every(1).second.do(print(1))


@app.on_edited_message(filters.bot)
async def edited(_, message: types.Message):
    text = str(message.text)
    # print(text)
    scrap(text, 10, 0.5, 1000)
    await asyncio.sleep(2)
    await message.click("Refresh")
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    await app.send_message(chat_id, "🔎 Orderbook")
    sleep(2)


# @app.on_message(filters.bot)
# async def get_qry(_, message: types.Message):
#     msg = str(message.text)
#     with open("file.txt", "w", encoding="utf-8") as file:
#         file.write(msg)
#     # print(msg.split("#"))
#     print("--" * 30)
#     # while True:
#     #     await message.click("Refresh")
#     #     print("clicked")
#     #     sleep(1)

# @app.on_edited_message(filters.bot)
# async def get_updated(_, message: types.Message):
#     text = str(message.text)
#
#     async def job(_, msg: types.Message):
#         return await message.click("Refresh")
#
#     if scrap(text, 10, 0.8, 1000):
#
#         await schedule.every(1).second.do(await job(_, message))
#     else:
#         print("Error")
# while True:
#     await message.click("Refresh")
#     sleep(1)
#     print("clicked")


#
#
# @app.on_message(filters.command("type", prefixes=".") & filters.me)
# async def eho(_, msg):
#     orig_text = msg.text.split(".type ", maxsplit=1)[1]
#     text = orig_text
#     tbp = ""  # to be printed
#     typing_symbol = "|"
#
#     while tbp != orig_text:
#         try:
#             await msg.edit(tbp + typing_symbol)
#             sleep(0.05)  # 50 ms
#
#             tbp = tbp + text[0]
#             text = text[1:]
#
#             await msg.edit(tbp)
#             sleep(0.05)
#
#         except FloodWait as e:
#             sleep(e.value)
#
#
# @app.on_message(filters.command("spam", prefixes=".") & filters.me)
# async def spam(_, msg):
#     orig_text = msg.text.split(".spam ", maxsplit=1)[1]
#     text = orig_text
#     await msg.delete()
#     try:
#         for i in range(12):
#             await msg.reply(text)
#     except FloodWait as e:
#         sleep(e.value)


@app.on_message(filters.command("payed", prefixes=".") & filters.me)
async def payed(_, message: types.Message):
    info = reader("head_db.json")[-1]
    info["payed"] = True
    add_in_json("head_db.json", [info])
    await message.reply("Ok")
    chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id = chat_id.id
    await app.send_message(chat_id, "🔎 Orderbook")
    sleep(1.5)


if __name__ == '__main__':
    app.run()
