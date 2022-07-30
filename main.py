from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from time import sleep
import json
from config import *

app = Client("Влад", api_hash=api_hash_v, api_id=api_id_v)


@app.on_message(filters.command("start", prefixes=".") & filters.me)
async def start_command(_, message: types.Message):
    chat_id = message.chat.id
    await app.send_message(chat_id, "Я запущений")
    dct = types.Chat = await app.get_chat("Kuna Code Bot")
    chat_id1 = dct.id
    await app.send_message(chat_id1, "🔎 Orderbook")
    sleep(0.05)


@app.on_message(filters.bot)
async def get_qry(_, message: types.Message):
    msg = str(message.text)
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write(msg)
    # print(msg.split("#"))
    print("--" * 30)
    # while True:
    #     await message.click("Refresh")
    #     print("clicked")
    #     sleep(1)


@app.on_edited_message(filters.bot)
async def get_updated(_, message: types.Message):
    print(str(message.text).split("#"))
    print("--" * 30)
    # while True:
    #     await message.click("Refresh")
    #     sleep(1)
    #     print("clicked")


# @app.on_message(filters.command("type", prefixes=".") & filters.me)
# async def eho(_, msg):
#     orig_text = msg.text.split(".type ", maxsplit=1)[1]
#     text = orig_text
#     tbp = ""  # to be printed
#     typing_symbol = "▒"
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


if __name__ == '__main__':
    app.run()
