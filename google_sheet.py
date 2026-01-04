import os, json, gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def add_to_sheet(data):
    print("📊 Google Sheet write started")

    sa_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    if not sa_json or not sheet_id:
        raise Exception("Missing GOOGLE_SERVICE_ACCOUNT_JSON or GOOGLE_SHEET_ID")

    creds = Credentials.from_service_account_info(
        json.loads(sa_json),
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )

    client = gspread.authorize(creds)

    # 🔥 OPEN BY ID (GUARANTEED)
    sheet = client.open_by_key(sheet_id).worksheet("Workshop Enrollments")

    sheet.append_row([
        data["name"],
        data["email"],
        data["phone"],
        data["course"],
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Website"
    ])

    print("✅ Google Sheet row added")


