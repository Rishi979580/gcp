import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_KEY, SENDER_EMAIL
from pathlib import Path

def load_template(name, data):
    html = Path("templates") / name
    content = html.read_text(encoding="utf-8")
    for k, v in data.items():
        content = content.replace(f"{{{{{k}}}}}", str(v))
    return content

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=30) as server:
        server.login(SMTP_USER, SMTP_KEY)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

    print(f"✅ Email sent to {to_email}")
