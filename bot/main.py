import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from api import create_user, get_birthdays, get_admins
import schedule
import time

load_dotenv('.botenv')

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    create_user(message.from_user.first_name, message.from_user.id, message.from_user.username)


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer("Available commands:\n /start \n /help")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def send_birthday_reminder():
    birthdays = get_birthdays()
    admins = get_admins()

    for admin in admins:
        for birthday in birthdays:
            message = f'Bugun {birthday["first_name"]} {birthday["last_name"]} ning tug\'ilgan kuni.\nYosh:{birthday["age"]}\nTu\'ilgan sana:{birthday["birthday"]}'
            await bot.send_photo(
                admin['user_id'], birthday['image'], caption=message,
            )


schedule.every().day.at("10:38", 'Asia/Tashkent').do(lambda: asyncio.run(send_birthday_reminder()))
while True:
    schedule.run_pending()
    time.sleep(1)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


