import asyncio
import sys
from aiohttp import web
from app.src.main.res.xml.config import settings
from app.src.main.media.grab.os.di.container import container
from app.src.main.media.grab.os.ui.home.handler import router as home_router
from app.src.main.media.grab.os.ui.paste.handler import router as paste_router
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# یک وب‌سرور بسیار سبک برای گول زدن Hugging Face (پورت 7860)
async def health_check(request):
    return web.Response(text="MediaGrab Bot is running smoothly!")

async def main():
    if not settings.BOT_TOKEN:
        print("Error: BOT_TOKEN is missing in environment variables.")
        sys.exit(1)

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    dp.include_router(home_router)
    dp.include_router(paste_router)
    
    print("MediaGrab Bot is starting... Core initialized.")
    
    # راه‌اندازی وب‌سرور فیک در پس‌زمینه
    app_web = web.Application()
    app_web.router.add_get("/", health_check)
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, port=7860)
    await site.start()
    print("Fake Web Server started on port 7860 to keep the Space alive.")

    # اجرای ربات تلگرام
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped gracefully.")
