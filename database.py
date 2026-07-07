<<<<<<< HEAD
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

=======
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

>>>>>>> 8bf753ab96844de6f412956b5129f8d13d0c50c5
print("Database Created Successfully")