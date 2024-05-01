from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv
import os
import logging

BOT_TOKEN = '7057532692:AAHwUixvbpFE5Zu3mcDAWIXAlkzIhvbQcvo'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЭто ЭХО"!\nНапиши мне')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

@dp.message(F.sticker)
async def get_sticker(message: Message):
    await message.answer('Стикер классный! Жаль такого у меня нет :(')

if __name__ == '__main__':
    dp.run_polling(bot)