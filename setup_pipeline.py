
import sqlite3
import csv
import os

db_path = '/Users/dylancleary/Projects/autoprod-relaunch/pipeline.db'
csv_path = '/Users/dylancleary/Projects/autoprod-relaunch/leads_v1.csv'

# Delete if exists to avoid double import during testing
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        industry TEXT,
        location TEXT,
        contact_role TEXT,
        bespoke_angle TEXT,
        comms_draft TEXT,
        status TEXT DEFAULT 'pending',
        sent_at TIMESTAMP,
        reply_received BOOLEAN DEFAULT 0,
        deal_value REAL DEFAULT 0,
        deal_stage TEXT DEFAULT 'lead'
    )
''')

# Load from CSV
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        cursor.execute('''
            INSERT INTO leads (company, industry, location, contact_role, bespoke_angle, comms_draft)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row['company'], row['industry'], row['location'], row['contact_role'], row['bespoke_angle'], row['comms_draft']))
        count += 1

conn.commit()
conn.close()

print(f"Database created and {count} leads imported.")
