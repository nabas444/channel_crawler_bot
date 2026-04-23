import asyncio
from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@AT_Tech_stream"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="Hello 🚀 Your bot is working!")

if __name__ == "__main__":
    asyncio.run(main())