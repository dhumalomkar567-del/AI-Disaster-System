import sqlite3
import os

# database folder 
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/disaster.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    rainfall REAL,
    risk TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")