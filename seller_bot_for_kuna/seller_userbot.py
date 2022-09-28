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

#
# def create_kuna_code(price: int):
#     auth = ""
#     headers = {"content-type": "application/json", "kun-apikey": "wI1G7NLzTycc4tyyJ4Hm8VBz76gnxqzKvmOxApcW"}
#     data = {"amount*": price, "currency*": "UAH"}
#     info = requests.get(f"https://api.kuna.io/v3/auth/kuna_codes", data=data, headers=headers)
#     # info = json.load(info)
#     print(info.content)
#
#
# create_kuna_code(25)
app = Client("me", api_id="14437576", api_hash="407794b728e894057cb4ef7545a03942")

app.start()
app.send_message(786805975, "/start")
chat_id = types.Chat.id = app.get_chat("Kuna Code Bot")
print(chat_id)
app.stop()



