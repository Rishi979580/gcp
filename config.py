# config.py
import os

SMTP_HOST = os.getenv("BREVO_SMTP_HOST")
SMTP_PORT = int(os.getenv("BREVO_SMTP_PORT", "465"))
SMTP_USER = os.getenv("BREVO_SMTP_USER")
SMTP_KEY  = os.getenv("BREVO_SMTP_KEY")

SENDER_EMAIL = os.getenv("SENDER_EMAIL")

# 🔥 CRITICAL FIX
SECRET_KEY = os.getenv("SECRET_KEY", "").strip()
