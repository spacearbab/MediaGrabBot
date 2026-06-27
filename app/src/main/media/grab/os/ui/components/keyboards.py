from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.src.main.media.grab.os.data.model.models import MediaInfo

def format_buttons(media: MediaInfo) -> InlineKeyboardMarkup:
    """
    ساخت کیبورد شیشه‌ای برای انتخاب کیفیت.
    دقیقاً مشابه لیست فرمت‌هایی که در اپ اندروید نمایش داده می‌شود.
    """
    keyboard = []
    
    # نمایش فرمت‌های ویدیویی (ترکیب صدا و تصویر)
    for f in media.progressive_formats[-4:]: # آخرین 4 کیفیت (بهترین‌ها)
        size_mb = f.filesize / (1024 * 1024)
        text = f"🎥 {f.resolution} ({size_mb:.1f} MB)"
        callback_data = f"dl_{f.format_id}"[:64] # محدودیت تلگرام روی 64 کاراکتر
        keyboard.append([InlineKeyboardButton(text=text, callback_data=callback_data)])
        
    # نمایش فرمت‌های صوتی فقط
    if media.audio_formats:
        best_audio = media.audio_formats[-1]
        size_mb = best_audio.filesize / (1024 * 1024)
        text = f"🎧 MP3 ({size_mb:.1f} MB)"
        callback_data = f"dl_{best_audio.format_id}"[:64]
        keyboard.append([InlineKeyboardButton(text=text, callback_data=callback_data)])
        
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
