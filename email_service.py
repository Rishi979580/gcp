import smtplib
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_KEY, SENDER_EMAIL
from pathlib import Path


def load_template(template_name: str, data: dict):
    template_path = Path("templates") / template_name
    html = template_path.read_text(encoding="utf-8")

    for key, value in data.items():
        html = html.replace(f"{{{{{key}}}}}", value)

    return html


def send_email(to_email, subject, body, is_html=False):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    if is_html:
        msg.add_alternative(body, subtype="html")
    else:
        msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_KEY)
        server.send_message(msg)
        