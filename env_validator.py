"""
.env dosyasındaki zorunlu çevresel değişkenleri kontrol eder.
"""
import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_KEYS = [
    "OPENAI_API_KEY",
    "ADMIN_EMAIL",
    "ADMIN_PASSWORD",
    "SMTP_EMAIL",
    "SMTP_PASSWORD",
    "LICENSE_KEY"
]

def validate_env():
    missing = []
    for key in REQUIRED_KEYS:
        if not os.getenv(key):
            missing.append(key)
    if missing:
        print("Eksik .env anahtarları:", ", ".join(missing))
        return False
    return True
