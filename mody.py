from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "21511060")
APP_HASH = os.environ.get("APP_HASH", "b2a2178e131fc47896c65d2d5e0c1faa")
SESSION = os.environ.get("SESSION")
elhzeyba = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
elhzeyba.start()
