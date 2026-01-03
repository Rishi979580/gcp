# 🚀 Python Automation – Email Trigger API

A production-ready Python automation project that triggers **Admin Alert** and **User Confirmation emails** when a user enrolls for a workshop from a website.

This project is built using **FastAPI**, **SMTP (Brevo)**, and is designed to run locally, on **GCP Cloud Shell**, or on **Cloud Run (Dockerized)**.

---

## 📁 Project Structure

```
python_automation_project
│
├── config.py                # Environment & SMTP configuration
├── email_service.py         # Email sending + HTML template loader
├── main.py                  # FastAPI application (API entry point)
├── schemas.py               # Pydantic request schemas
├── requirements.txt         # Python dependencies
├── templates
│   ├── admin_alert.html     # Admin notification email template
│   └── user_confirmation.html # User confirmation email template
├── notes                    # Learning & reference notes
└── README.md
```

---

## ⚙️ Prerequisites

* Python 3.10+
* Virtual Environment (recommended)
* Brevo SMTP credentials
* GCP Cloud Shell (optional)

---

## 📦 Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv email-validator
```

OR (recommended):

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the project root:

```env
BREVO_SMTP_HOST=smtp-relay.brevo.com
BREVO_SMTP_PORT=587
BREVO_SMTP_USER=your_brevo_username
BREVO_SMTP_KEY=your_brevo_smtp_key
SENDER_EMAIL=no-reply@yourdomain.com
```

---

## ▶️ Run the Application

### Local / Cloud Shell

```bash
uvicorn main:app --reload --port 8080
```

### Cloud Shell Access

Use **Web Preview → Port 8080**

Example URL:

```
https://8080-<random>-cloudshell.dev
```

---

## 📘 API Documentation (Swagger UI)

Open in browser:

```
https://8080-<random>-cloudshell.dev/docs
```

---

## 🧪 Test `/enroll` API (Step-by-Step)

1. Open `/docs`
2. Select `POST /enroll`
3. Click **Try it out**
4. Paste JSON:

```json
{
  "name": "Rishikesh",
  "email": "test@gmail.com",
  "workshop": "Python Automation Workshop"
}
```

5. Click **Execute**

---

## ✅ Expected Result

### API Response

```json
{
  "status": "success"
}
```

### Emails Triggered

* 📩 Admin Alert Email
* 📩 User Confirmation Email

---

## 🌐 API Endpoints

| Method | Endpoint  | Description                         |
| ------ | --------- | ----------------------------------- |
| GET    | `/`       | Health check (optional)             |
| POST   | `/enroll` | Workshop enrollment & email trigger |
| GET    | `/docs`   | Swagger UI                          |

---

## 🧠 Notes

* `localhost:8080` does **not work in Cloud Shell browser**
* Always use **Cloud Shell Web Preview URL**
* `EmailStr` requires `email-validator` package

---

## 🚀 Production Deployment (Next Steps)

* Dockerize the application
* Deploy on **GCP Cloud Run**
* Connect frontend (React / HTML form)
* Add Google Sheet / Firebase lead storage
* Add WhatsApp or SMS notifications

---

## 👨‍💻 Author

**Rishikesh (FutureWay)**
Python Automation | Cloud | Data Analytics

---

✅ This project follows real-world production practices used in SaaS and EdTech systems.
