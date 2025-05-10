"""
E-posta gönderimi için SMTP kullanarak üyeye doğrulama kodu yollar.
"""
import smtplib
import ssl
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.getenv("SMTP_EMAIL")
EMAIL_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_verification_code(receiver_email, code):
    msg = EmailMessage()
    msg["Subject"] = "Harita SEO Asistanı - Doğrulama Kodu"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg.set_content(f"Giriş için doğrulama kodunuz: {code}")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
