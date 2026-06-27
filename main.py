import asyncio
import sys
from app.src.main.res.xml.config import settings
from app.src.main.media.grab.os.di.container import container
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

async def main():
    if not settings.BOT_TOKEN:
        print("Error: BOT_TOKEN is missing in environment variables.")
        sys.exit(1)

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    print("Initializing MediaGrab Core...")
    _ = container.extractor
    print("Core initialized successfully. Bot is running...")

    # هندلرهای UI در مرحله بعد اینجا اضافه می‌شوند
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped gracefully.")
