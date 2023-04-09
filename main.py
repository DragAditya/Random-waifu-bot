from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN

from waifupics import waifu_nsfw, waifu_sfw

bot = Bot(token=BOT_TOKEN)
dp= Dispatcher(bot)

button_hi = KeyboardButton('Привет! 👋')

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('/sfw')
).add(
    KeyboardButton('/nsfw')
)


@dp.message_handler(commands=['start'])
async def nsf(message: types.Message):
    await message.reply('This bot sends a random pic with random waifu! <3\nBot supports two modes: "sfw" and "nsfw"', reply_markup=markup_request)

@dp.message_handler(commands=['sfw'])
async def nsf(message: types.Message):
    response = await waifu_sfw()
    await message.reply(f'<a href="{response}">Imgae URL</a>', reply_markup=markup_request, parse_mode='HTML')

@dp.message_handler(commands=['nsfw'])    
async def nsf(message: types.Message):
    response = await waifu_nsfw()
    await message.reply(f'<a href="{response}">Imgae URL</a>', reply_markup=markup_request, parse_mode='HTML')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)