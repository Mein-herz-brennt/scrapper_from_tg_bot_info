import aioschedule as schedule
from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait
import asyncio
import tgcrypto
from config import *
from helper_checker import *
from scrapper import reader

deal_link = ""
# TODO
app = Client("my_friend", api_id=api_id_b, api_hash=api_hash_b)


def checked():
    if checker():
        return True
    else:
        return False


# if schedule.every().second.do(checker()):
#     chat_id = types.Chat = app.get_chat("Kuna Code Bot")
#     deal = reader("last_result.json")[-1]["link"]
#     deal_link = deal
#     await app.send_message(chat_id.id, deal)

#
@app.on_message(filters.bot)
async def get_info_about_deal(_, message: types.Message):
    global deal_link
    if "you are going to accept order " in message.text:
        chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
        chat_id = chat_id.id
        await app.send_message(chat_id, "📥 Pay")
    elif message.text.startswith("We`re in a deal creation."):
        pass
    elif len(message.text) == 16:
        info = reader("last_result.json")
        info1 = reader("result.json")
        if info[-1]["link"] == deal_link:
            # msg = f"""Order: {info[-1]["#"]}\n
            #           Prise: {info[-1]["min"]} | {info[-1]["max"]}\n
            #           Percents: {info[-1]["percent"]}%\n
            #           User: {info[-1]["user"]}\n
            #           Bank: {info[-1]["bank"]}\n
            #           Link: {info[-1]["link"]}"""
            info[-1]["card"] = message.text
            info[-1]["payed"] = False
            add_in_json("head_db.json", [info[-1]])
            # await app.send_message(789402487, msg)
        else:
            for i in info1:
                if i["link"] == deal_link:
                    # msg = f"""Order: {i["#"]}\n
                    #           Prise: {i["min"]} | {i["max"]}\n
                    #           Percents: {i["percent"]}%\n
                    #           User: {i["user"]}\n
                    #           Bank: {i["bank"]}\n
                    #           Link: {i["link"]}"""
                    i["card"] = message.text
                    i["payed"] = False
                    add_in_json("head_db.json", [i])
        if await schedule.every().second.do(reader("head_db.json")[-1]["payed"]):
            await message.click("🤝 I have paid")
    else:
        await message.forward(filters.me)
        # await app.send_message(789402487, msg)


#

# @app.on_message(filters.bot)  # filters.command("payed") & filters.me
# async def payed(_, message: types.Message):
#     global last_message_id
#     chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
#     chat_id = chat_id.id
#     print(await app.get_inline_bot_results(chat_id))


# @app.on_message(filters.me)
# async def get(_, message: types.Message):
#     print(message.chat.id)


if __name__ == '__main__':
    app.run()
    while True:
        await schedule.run_pending()
