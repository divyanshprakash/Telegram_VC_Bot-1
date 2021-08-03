import asyncio
from pyrogram import Client, idle, filters
import os
from config import Config
from utils import mp, USERNAME, FFMPEG_PROCESSES
from pyrogram.raw import functions, types
import os
import sys
from threading import Thread
from signal import SIGINT
import subprocess
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
def stop_and_restart():
    bot.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)

bot.start()
run()
