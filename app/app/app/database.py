import sqlite3

def init_db():
    conn = sqlite3.connect("energy.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS energy_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        voltage REAL,
        current REAL,
        power REAL,
        energy REAL,
        timestamp REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_data(data):
    conn = sqlite3.connect("energy.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO energy_data (voltage, current, power, energy, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["voltage"],
        data["current"],
        data["power"],
        data["energy"],
        data["timestamp"]
    ))

    conn.commit()
    conn.close()
