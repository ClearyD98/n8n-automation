#!/usr/bin/env python3
"""autoprod client pipeline — handles bookings end-to-end"""
import sqlite3, smtplib, os, json
from email.mime.text import MIMEText
from datetime import datetime

DB = "/Users/dylancleary/Projects/autoprod-relaunch/pipeline.db"
ZOHO_USER = "allistair@autoprod.io"

def get_zoho_pass():
    return os.environ.get("ZOHO_PASSWORD", "")

def send_email(to, subject, body):
    pw = get_zoho_pass()
    if not pw: return False
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = f"autoprod <{ZOHO_USER}>"
    msg["To"] = to
    with smtplib.SMTP("smtp.zoho.eu", 587, timeout=15) as s:
        s.starttls(); s.login(ZOHO_USER, pw); s.send_message(msg)
    return True

def onboard_client(name, email, service, amount):
    """Send welcome email + log to CRM"""
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY, name TEXT, email TEXT, service TEXT,
        amount REAL, status TEXT, booked_at TIMESTAMP, notes TEXT)""")
    conn.execute("INSERT INTO clients (name,email,service,amount,status,booked_at) VALUES (?,?,?,?,?,CURRENT_TIMESTAMP)",
                 (name, email, service, amount, "onboarded"))
    conn.commit()
    
    body = f"""Hi {name},

Thanks for booking {service} with autoprod.

What happens next:
1. I'll review your booking and send a calendar invite within 24 hours
2. Sessions are held at The Carriageworks, Sheriff Street, Dublin 1 (or virtual)
3. You'll receive a brief prep questionnaire — it takes 5 minutes

All sessions are evenings (after 6pm) or weekends to fit around your schedule.

If you have any questions, reply to this email.

— Dylan
autoprod.io"""
    
    send_email(email, f"Welcome to autoprod — {service}", body)
    print(f"✓ Onboarded {name} ({service}, €{amount})")
    conn.close()

if __name__ == "__main__":
    print("autoprod pipeline handler ready")
    print("Usage: python3 pipeline_handler.py")
