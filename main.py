from email_service import send_email

def main():
    send_email(
        to_email="info.deshdisha@gmail.com",   # apna email yahan daalo
        subject="Brevo SMTP Test Email",
        body=(
            "Hello 👋\n\n"
            "This is a test email sent successfully using:\n"
            "Brevo SMTP + Python automation.\n\n"
            "If you received this email, your SMTP setup is working correctly.\n\n"
            "Regards,\n"
            "Python Automation System"
        )
    )

if __name__ == "__main__":
    main()

# source venv/bin/activate
# python main.py