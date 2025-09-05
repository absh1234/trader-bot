# Trading Bot MVP

1. فایل .env را از .env.example بساز و توکن تلگرام و کلیدهای صرافی (برای تست) را وارد کن.
2. اجرا در لوکال (پایتون):
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   export TELEGRAM_TOKEN=...
   python -m app.main

یا با داکر:
   docker compose up --build

پیش‌فرض: Binance Testnet. تغییر در config یا متغیرهای محیطی.
