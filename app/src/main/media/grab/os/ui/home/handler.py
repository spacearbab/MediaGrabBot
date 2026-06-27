from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    هندلر دستور /start. معادل Onboarding Fragment در اندروید.
    """
    welcome_text = (
        "👋 <b>به ربات MediaGrab خوش آمدی!</b>\n\n"
        "🎬 این ربات توانایی دانلود از بیش از 1000 سایت (یوتیوب، اینستاگرام، تیک‌تاک و...) را دارد.\n"
        "🔗 کافیست لینک ویدیو یا موسیقی مورد نظرت را اینجا بفرستی تا معجزه ببینیم!\n\n"
        "⚙️ <i>نسخه هسته: Pro v1.0</i>"
    )
    await message.answer(welcome_text)
