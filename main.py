from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import EnrollRequest
from email_service import send_email, load_template
from google_sheet import add_to_sheet
from config import SECRET_KEY

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "https://skill.futureway.in"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/enroll")
def enroll(data: EnrollRequest, x_secret_key: str = Header(None)):
    # 🔍 TEMP DEBUG (remove later)
    print("🔑 HEADER =", repr(x_secret_key))
    print("🔐 ENV    =", repr(SECRET_KEY))

    if not x_secret_key or x_secret_key.strip() != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid secret key")

    payload = {
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "course": data.course
    }

    try:
        add_to_sheet(payload)
    except Exception as e:
        print("❌ Sheet error:", e)

    try:
        admin_html = load_template("admin_alert.html", payload)
        send_email("futureway.in@gmail.com", "🔥 New Workshop Enrollment", admin_html)
    except Exception as e:
        print("❌ Admin mail error:", e)

    try:
        user_html = load_template("user_confirmation.html", payload)
        send_email(data.email, "✅ Registration Confirmed", user_html)
    except Exception as e:
        print("❌ User mail error:", e)

    return {"status": "success"}
