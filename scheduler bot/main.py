import asyncio
from aiogram import Bot, Dispatcher
from appp.handlers import router

# Function to safely retrieve the bot token
def get_bot_token():
    try:
        with open('scheduler bot/token_2.txt', 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        raise RuntimeError("Token file not found. Please provide a valid token file.")

# Initialize bot and dispatcher
TOKEN = get_bot_token()
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)


# Polling - continuous work loop for the bot
async def main():
    try:
        # Start polling
        await dp.start_polling(bot)
    finally:
        # Ensure resources are properly cleaned up
        await bot.session.close()
        print("Bot shut down gracefully.")


# Run main() if the script is executed directly
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped due to user interrupt or system exit.")