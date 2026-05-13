import time

from generator import generate_reading
from analytics import detect_anomalies
from database import init_db, insert_data

# Initialize database once
init_db()

print("⚡ Smart Grid System Starting...")

while True:
    # 1. Generate fake sensor data
    data = generate_reading()

    # 2. Run analytics (check for problems)
    alerts = detect_anomalies(data)

    # 3. Save to database
    insert_data(data)

    # 4. Print live data
    print("\n📊 New Reading:")
    print(data)

    # 5. Print alerts if any
    if alerts:
        print("🚨 ALERTS:")
        for a in alerts:
            print("-", a)

    # 6. Wait 1 second (simulates real-time system)
    time.sleep(1)
