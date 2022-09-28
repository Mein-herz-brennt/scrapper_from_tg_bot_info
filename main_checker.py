import time
from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from config import *
from helper_checker import *
from scrapper import reader, check_json, add_in_json

app = Client("Nastya", api_id=api_id_5, api_hash=api_hash_5)

deal_link = []
counter = True
link_ = ""
card = ""
information = ""


@app.on_message(filters.regex("/deal"))
async def start(_, message: types.Message):
    global deal_link, link_
    if message.chat.id == -1001687565244:
        link = message.text
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        if link not in deal_link:
            await app.send_message(chat_id, link)
            time.sleep(0.05)
            await app.send_message(chat_id, "📥 Pay")
            deal_link.append(link)


@app.on_message(filters.bot & filters.text)
async def get_info_about_deal(_, message: types.Message):
    global deal_link, counter, link_, card, information
    if "you are going to accept order" in str(message.text):
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        await app.send_message(chat_id, "📥 Pay")
        inf = message.text.split('\n')
        if "Markup" in message.text or "Discount" in message.text:
            information = inf[6]
        else:
            information = inf[2] + "\n"
    elif message.text.startswith("We`re in a deal creation"):
        try:
            await app.send_message(424079525, f"🟨Жду карту!")
        except Exception:
            print(0)
    elif "Waiting for seller's confirmation" in str(message.text):
        try:
            await app.send_message(424079525, f"🟩Жду Код!")
        except Exception:
            print(0)
    elif message.text.startswith("Please pay"):
        information += message.text.split("\n")[0]
    elif len(message.text) == 16:
        card = message.text
        try:
            await app.send_message(424079525, information + "\n" + f"💳<code>{message.text}</code>")
        except Exception:
            print(0)
    elif message.text.endswith("KCode"):
        code = message.text
        try:
            await app.send_message(424079525, f"KunaCode: <code>{code}</code>")
        except Exception:
            print(0)


@app.on_message(filters.command("ok", prefixes="."))
async def last_click(_, msg: types.Message):
    global card
    if msg.from_user.id == 424079525:
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        async for message in app.search_messages(chat_id, query=card):
            try:
                await message.click("🤝 I have paid")
                await msg.reply("Нажато!")
            except Exception:
                print(0)


@app.on_message(filters.command("cancel", prefixes="."))
async def cancel(_, message: types.Message):
    if message.from_user.id == 424079525:
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        await app.send_message(chat_id, "❌ Cancel deal")
        time.sleep(1.5)
        await app.send_message(chat_id, "1")


@app.on_message(filters.photo)
async def send_photo(_, message: types.Message):
    if message.from_user.id == 424079525:
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        await app.send_message(chat_id, "📷 Upload screenshot of payment")
        time.sleep(1.5)
        await message.forward(chat_id)


if __name__ == '__main__':
    app.run()
