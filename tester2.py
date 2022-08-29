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

# app = Client("Nastya", api_id=api_id_5, api_hash=api_hash_5)
TOKEN = "1510499721:AAE2yMV1IjH2pYZrltd-z0oXskc-80mf3UA"
# token = "5669125136:AAFztoGGP94HY7aPXqqxMtZWYCO6S5MaK54"

# print(req.content)

app = Client("my_second", api_id="18697047", api_hash="ac87134aea991710119ca75ca72f56b0")
# app0 = Client("me", api_id="14437576", api_hash="407794b728e894057cb4ef7545a03942")


# async def send_update(app: Client):
#     await app.start()
#     chat_id = types.Chat = await app.get_chat("Kuna Code Bot")
#     chat_id = chat_id.id
#     await app.send_message(chat_id, "/start")
#     await app.stop()


