FROM python:3.11-slim

# نصب ابزارهای سیستم و ffmpeg برای پردازش رسانه
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# کپی کردن فایل نیازمندی‌ها و نصب کتابخانه‌های پایتون
COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل سورس کد پروژه
COPY . .

# دستور اجرای ربات
CMD ["python", "main.py"]
