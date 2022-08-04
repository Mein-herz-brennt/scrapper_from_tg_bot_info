from helper_checker import *
from scrapper import *
import schedule
import asyncio

schedule.every().second.do(checker)
schedule.every().second.do(check_json)

while True:
    schedule.run_pending()
    asyncio.sleep(0.01)

