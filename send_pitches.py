#!/usr/bin/env python3
"""autoprod direct outreach — sends real pitches to Irish companies via Proton Bridge"""

import smtplib, sqlite3, time, subprocess, sys, os
from email.mime.text import MIMEText

SMTP_HOST = "smtp.zoho.eu"
SMTP_PORT = 587
FROM_EMAIL = "allistair@autoprod.io"
ZOHO_PASS = "Depress3-Labrador0-Siding9-Ungraded0-Citric2" 
FROM_NAME = "Dylan Cleary"
REPLY_TO = "dylan@autoprod.io"
DB_PATH = os.path.expanduser("~/Projects/autoprod-relaunch/pipeline.db")

# LIVE STRIPE PAYMENT LINKS
STRIPE_AUDIT = "https://buy.stripe.com/9B67sM3AI8Ij4D91jK7ss0b"
STRIPE_STRATEGY = "https://buy.stripe.com/9B6fZi7QYcYz2v18Mc7ss0a"

# Irish companies with REAL verifiable email addresses
TARGETS = [
    # Law firms — most have public partner emails
    ("info@mhc.ie", "Mason Hayes & Curran", "Legal", 
     "I noticed MHC has been expanding its tech practice. The EU AI Act enforcement deadline is August 2026 — most Irish law firms will need AI governance frameworks for their corporate clients. We build these for €2,500 flat."),
    
    ("info@algoodbody.com", "A&L Goodbody", "Legal",
     "A&L Goodbody's regulatory team will be fielding EU AI Act questions from every corporate client starting this year. We provide a turnkey AI governance assessment — €250 audit, €2,500 full framework. DPC-aligned, board-ready."),
    
    ("info@matheson.com", "Matheson LLP", "Legal",
     "Matheson is Ireland's largest law firm. Your corporate clients need AI Act compliance frameworks. We build them — €250 readiness audit, €2,500 full governance package. Irish-specific, DPC-aligned."),
    
    # Insurance — regulated, AI Act applies directly
    ("info@fbd.ie", "FBD Insurance", "Insurance",
     "FBD is probably already looking at the EU AI Act. Insurance is squarely in scope for high-risk AI classification. We offer a fixed-price AI governance framework — €250 audit to start. Irish-built, DPC-aligned."),
    
    ("info@irishlife.ie", "Irish Life", "Insurance",
     "Irish Life's underwriting and claims processes are exactly the type of systems the EU AI Act regulates. We provide a €250 fixed-price AI readiness audit — board-ready report, gap analysis, compliance roadmap."),
    
    # Banking
    ("info@ptsb.ie", "Permanent TSB", "Banking",
     "PTSB is the right size for this — big enough to need AI governance, small enough that Big 4 consulting is overkill. We provide fixed-price AI Act compliance frameworks. €250 to start."),
    
    # Construction/Engineering
    ("info@johnsiskandson.ie", "Sisk Group", "Construction",
     "Construction is catching up on digital transformation fast. The EU AI Act applies to any AI in project management, safety systems, or hiring. We offer a €250 AI readiness audit — board-ready, construction-specific."),
    
    ("info@bamireland.ie", "BAM Ireland", "Construction",
     "BAM Ireland likely uses AI in project scheduling, risk assessment, and HR. The EU AI Act classifies much of this as high-risk. We provide a turnkey compliance framework — €250 audit to start."),
    
    # Retail — supply chain AI is in scope
    ("info@musgravegroup.com", "Musgrave Group", "Retail",
     "Musgrave's supply chain is exactly where AI and EU regulation intersect. The AI Act regulates automated decision-making in logistics. We offer a fixed-price €250 compliance assessment — Irish-built, board-ready."),
    
    # Energy — semi-state, regulatory pressure
    ("info@esb.ie", "ESB Group", "Energy",
     "ESB uses AI in grid management and customer operations. Both are potentially high-risk under the EU AI Act. We provide a €250 fixed-price AI readiness audit — tailored for semi-state regulatory requirements."),
    
    # Logistics
    ("info@anpost.ie", "An Post", "Logistics",
     "An Post's logistics and sorting systems likely use AI — squarely in scope for EU AI Act compliance. We offer a €250 fixed-price readiness audit. DPC-aligned, semi-state appropriate."),
]

def get_bridge_password():
    result = subprocess.run(
        ["security", "find-generic-password", "-s", "proton-bridge-info-dylancleary", "-w"],
        capture_output=True, text=True
    )
    pw = result.stdout.strip()
    if not pw:
        raise RuntimeError("Could not retrieve Proton Bridge password from keychain")
    return pw

def send_email(to_email, company_name, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["Reply-To"] = REPLY_TO
    msg["To"] = to_email
    
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.login(FROM_EMAIL, ZOHO_PASS)
            server.send_message(msg)
            print(f"✓ Sent to {company_name} <{to_email}>")
            return True
    except Exception as e:
        print(f"✗ Failed {company_name}: {e}")
        return False

def main(max_send=5):
    sent = 0
    for email, company, industry, pitch in TARGETS:
        if sent >= max_send:
            break
        
        subject = f"EU AI Act compliance — {company}"
        
        # Build the email body
        body = f"""Hi {company} team,

{pitch}

**What you get:**
→ AI Readiness Audit (€250): Complete inventory of your AI systems, risk classification against the EU AI Act, gap analysis, board-ready report. 2 weeks.

→ Full Governance Framework (€5,000): Everything above plus complete policy suite, 90-day implementation roadmap, team training, DPC-aligned documentation. 4 weeks.

Ready to start? Book the audit here:
{STRIPE_AUDIT}

Or reply to this email — happy to schedule a 15-minute call.

Best,
Dylan Cleary
autoprod.io
AI Mastery for Irish Enterprise

—
This is a one-time outreach. If you're not the right person, please forward to your compliance/legal/IT team."""
        
        if send_email(email, company, subject, body):
            sent += 1
        
        time.sleep(5)  # Throttle to avoid Proton rate limits
    
    print(f"\nDone. {sent} emails sent.")
    return sent

if __name__ == "__main__":
    count = main(max_send=5)
    print(f"Stripe links: {STRIPE_AUDIT}")
