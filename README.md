# Waifu Bot
This is a async Telegram bot that sends a random picture of a waifu (anime girl) in either SFW (safe for work) or NSFW (not safe for work) mode. It uses the [Waifu Pics API](https://waifu.pics/docs) to fetch the images.
[(my bot on free hosting)](https://t.me/randomanimewaifupicbot)

![example](https://sun9-52.userapi.com/impg/JAgPCnELOREB6nuZZm0dy44ldhEaMYWDP6TA4A/O__TasaT2c0.jpg?size=462x693&quality=96&sign=90535a4777746217c29d8e140afb190a&type=album)

## Getting Started
To use this bot, you need to have a Telegram account and create a new bot on Telegram. You can follow the instructions on the BotFather page to create a new bot and get a token.

Once you have the bot token, create a config.py file and add the following line:
```python
BOT_TOKEN = 'Your_telegram_token'
```
Replace Your_telegram_token with your actual bot token.

You also need to install the required dependencies. You can do this by running the following command:
```
pip install -r requirements.txt
```

## How to Use
To start using the bot, send the /start command. The bot will respond with a message that explains how to use it. You can then use the /sfw or /nsfw command to get a random SFW or NSFW waifu picture, respectively.

## Code Overview
The bot is implemented using the aiogram library, which provides a high-level framework for building Telegram bots in Python.

The main.py file contains the main code for the bot. It creates a Bot object and a Dispatcher object, and defines three message handlers for the /start, /sfw, and /nsfw commands. The message handlers use the waifu_sfw and waifu_nsfw functions from the waifupics module to fetch the images.

The waifupics.py module defines two functions, waifu_sfw and waifu_nsfw, which use the aiohttp library to fetch a random waifu image from the Waifu Pics API.

The config.py file contains the bot token, which is used by the main.py file to authenticate with the Telegram API.
