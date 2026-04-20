import asyncio
from telegram import Bot

BOT_TOKEN = "8736836984:AAFeKHHU2KFBcKpEz-NT1eXSwrZhLTn1LfY"
CHANNEL_ID = "@AT_Tech_stream"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="Hello 🚀 Your bot is working!")

if __name__ == "__main__":
    asyncio.run(main())