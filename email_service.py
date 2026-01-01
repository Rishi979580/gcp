import smtplib
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_KEY, SENDER_EMAIL


def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_KEY)
            server.send_message(msg)

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Error while sending email:", e)
