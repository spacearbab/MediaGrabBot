import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    لایه تنظیمات حرفه‌ای. معادل فایل‌های XML کانفیگ در اندروید.
    """
    BOT_TOKEN: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    ADMIN_ID: int = 4421308544  # آیدی عددی ادمین (شما)

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
