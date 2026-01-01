import os
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("BREVO_SMTP_HOST")
SMTP_PORT = int(os.getenv("BREVO_SMTP_PORT", 587))
SMTP_USER = os.getenv("BREVO_SMTP_USER")
SMTP_KEY = os.getenv("BREVO_SMTP_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
