import re
from aiogram import Router, F
from aiogram.types import Message
from app.src.main.media.grab.os.di.container import container
from app.src.main.media.grab.os.ui.components.keyboards import format_buttons

router = Router()

# الگویregex برای تشخیص لینک‌ها
URL_PATTERN = re.compile(r'https?://[^\s]+')

@router.message(F.text, URL_PATTERN.match)
async def handle_link(message: Message):
    """
    هندلر دریافت لینک. 
    ربات را در حالت انتظار (Processing) قرار می‌دهد و اطلاعات را استخراج می‌کند.
    """
    url = message.text.strip()
    processing_msg = await message.reply("⏳ <i>در حال پردازش لینک... صبر کنید.</i>")
    
    # استفاده از موتور استخراج (DI)
    extractor = container.extractor
    media_info = await extractor.extract(url)
    
    if not media_info:
        await processing_msg.edit_text("❌ خطا در استخراج لینک. ممکن است لینک نامعتبر باشد یا سایت پشتیبانی نشود.")
        return
        
    caption = (
        f"🎬 <b>{media_info.title}</b>\n\n"
        f"👤 <b>منتشرکننده:</b> {media_info.uploader}\n"
        f"⏱ <b>مدت زمان:</b> {media_info.duration // 60}:{media_info.duration % 60:02d}\n"
        f"🌐 <b>منبع:</b> {media_info.extractor}\n\n"
        f"👇 <i>کیفیت مورد نظر را برای دانلود انتخاب کنید:</i>"
    )
    
    keyboard = format_buttons(media_info)
    
    try:
        # ارسال عکس تامنیل همراه با دکمه‌ها
        if media_info.thumbnail:
            await message.answer_photo(
                photo=media_info.thumbnail,
                caption=caption,
                reply_markup=keyboard
            )
        else:
            await message.answer(text=caption, reply_markup=keyboard)
            
        await processing_msg.delete()
    except Exception as e:
        await processing_msg.edit_text(f"⚠️ خطا در نمایش اطلاعات: {e}")
