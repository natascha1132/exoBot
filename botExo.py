from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7057532692:AAHwUixvbpFE5Zu3mcDAWIXAlkzIhvbQcvo'


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()




# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')




# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )




# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)

async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)

async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)

async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)

async def send_video_note_echo(message: Message):
    await message.reply_video_note(message.video_note.file_id)

async def send_gif_echo(message: Message):
    await message.reply_gif(message.gif.file_id)
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)

async def send_emoji_echo(message: Message):
    await message.reply_emoji(message.emoji.file_id)
# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)




# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_document_echo, F.document)
dp.message.register(send_emoji_echo, F.emoji)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)