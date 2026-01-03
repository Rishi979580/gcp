from fastapi import FastAPI
from schemas import EnrollRequest
from email_service import send_email, load_template

app = FastAPI()

@app.post("/enroll")
def enroll(data: EnrollRequest):

    payload = {
        "name": data.name,
        "email": data.email,
        "workshop": data.workshop
    }

    # 1️⃣ Admin Alert
    admin_html = load_template("admin_alert.html", payload)
    send_email(
        to_email="futureway.in@gmail.com",
        subject="🔥 New Workshop Enrollment",
        body=admin_html,
        is_html=True
    )

    # 2️⃣ User Confirmation
    user_html = load_template("user_confirmation.html", payload)
    send_email(
        to_email=data.email,
        subject="✅ Enrollment Successful",
        body=user_html,
        is_html=True
    )

    return {"status": "success"}
