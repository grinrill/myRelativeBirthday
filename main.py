from datetime import datetime, timedelta

from telethon.sync import TelegramClient
from telethon import functions, types

# load config from config.yml
from yaml import safe_load

from logging import basicConfig, getLogger, INFO

basicConfig(level=INFO)
logger = getLogger(__name__)

with open("config.yml", "r") as f:
    config = safe_load(f)

# delta can specify weeks, days, hours relative to now
delta = timedelta(**config.get("delta", {}))
# date can specify year, month, day to set a specific birthday
# if a field is not specified, it will be taken from the current date + delta
# otherwise will override the current date + delta
date = config.get("date", {})
api_id = config["api_id"]
api_hash = config["api_hash"]

with TelegramClient("name", api_id, api_hash) as client:
    now = datetime.now()
    birthday = now + delta
    if year := date.get("year"):
        birthday = birthday.replace(year=year)
    if month := date.get("month"):
        birthday = birthday.replace(month=month)
    if day := date.get("day"):
        birthday = birthday.replace(day=day)
    client(
        functions.account.UpdateBirthdayRequest(
            birthday=types.Birthday(
                day=birthday.day, month=birthday.month, year=birthday.year
            )
        )
    )
    logger.info("Birthday set to %s", birthday.strftime("%Y-%m-%d"))
