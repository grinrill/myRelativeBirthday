from datetime import datetime, timedelta

from telethon.sync import TelegramClient
from telethon import functions, types

# load config from config.yml
from yaml import safe_load

with open("config.yml", "r") as f:
    config = safe_load(f)

delta = timedelta(**config.get("delta", {}))
api_id = config["api_id"]
api_hash = config["api_hash"]

with TelegramClient("name", api_id, api_hash) as client:
    now = datetime.now()
    birthday = now + delta
    client(
        functions.account.UpdateBirthdayRequest(
            birthday=types.Birthday(
                day=birthday.day, month=birthday.month, year=birthday.year
            )
        )
    )
