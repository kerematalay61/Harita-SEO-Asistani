"""
Programın lisans anahtarını kontrol eder. Geçerli değilse çalışmayı durdurur.
"""
import os
from dotenv import load_dotenv

load_dotenv()

VALID_LICENSE_KEYS = [
    "KEREM-SEO-2024-TRIAL",
    "KEREM-SEO-2025-PRO",
    "KEREM-SEO-UNLIMITED"
]

def is_license_valid():
    key = os.getenv("LICENSE_KEY")
    return key in VALID_LICENSE_KEYS
