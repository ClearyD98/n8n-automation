#!/usr/bin/env python3
"""autoprod mailer — sends outreach pitches via Proton Mail Bridge"""
import smtplib, sqlite3, time, subprocess, sys
from email.mime.text import MIMEText

SMTP_HOST = "127.0.0.1"
SMTP_PORT = 1025
FROM_EMAIL = "info@dylancleary.com"
FROM_NAME = "Dylan Cleary"
REPLY_TO = "dylan@autoprod.io"
DB_PATH = "/Users/dylancleary/Projects/autoprod-relaunch/pipeline.db"

def get_bridge_password():
    result = subprocess.run(
        ["security", "find-generic-password", "-s", "proton-bridge-info-dylancleary", "-w"],
        capture_output=True, text=True
    )
    pw = result.stdout.strip()
    if not pw:
        raise RuntimeError("Could not retrieve Proton Bridge password from keychain")
    return pw

def send_email(to_email, to_name, subject, body, password):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["Reply-To"] = REPLY_TO
    msg["To"] = to_email
    
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.login(FROM_EMAIL, password)
        server.send_message(msg)
        print(f"✓ Sent to {to_name} <{to_email}>")

def main(max_send=5):
    password = get_bridge_password()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, company, contact_role, comms_draft FROM leads WHERE status = 'pending' LIMIT ?",
        (max_send,)
    )
    leads = cursor.fetchall()
    
    if not leads:
        print("No pending leads found.")
        return
    
    print(f"Sending {len(leads)} outreach emails via info@dylancleary.com...")
    sent = 0
    
    for lead in leads:
        lead_id, company, contact_role, comms_draft = lead
        # Use a real recipient pattern — these go to info@ for now since we don't have direct contacts
        # In production, replace with actual contact email from CRM
        to_email = f"info@{company.lower().replace(' ', '').replace(',', '').replace('(', '').replace(')', '')}.com"
        to_name = contact_role
        
        subject = f"AI for {company}: Speed, Compliance, and the Future of Your Business"
        
        try:
            send_email(to_email, to_name, subject, comms_draft, password)
            cursor.execute(
                "UPDATE leads SET status = 'sent', sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (lead_id,)
            )
            conn.commit()
            sent += 1
            time.sleep(3)  # Throttle
        except Exception as e:
            print(f"✗ Failed {company}: {e}")
            cursor.execute(
                "UPDATE leads SET status = 'failed' WHERE id = ?",
                (lead_id,)
            )
            conn.commit()
    
    conn.close()
    print(f"\nDone. {sent}/{len(leads)} sent.")

if __name__ == "__main__":
    main()
