import time
from collections import deque

from generator import generate_reading
from analytics import detect_anomalies
from database import init_db, insert_data

# Initialize DB once
init_db()

print("⚡ Smart Grid REAL-TIME System Running...\n")

# Keep last readings in memory (for live feel / future dashboard)
live_buffer = deque(maxlen=20)

while True:
    start_time = time.time()

    # 1. Generate new sensor reading
    data = generate_reading()

    # 2. Run analytics immediately
    alerts = detect_anomalies(data)

    # 3. Store in database instantly
    insert_data(data)

    # 4. Store in live memory buffer
    live_buffer.append(data)

    # 5. Display live output (real-time feel)
    print("\n==============================")
    print("📊 LIVE GRID UPDATE")
    print("==============================")
    print(f"Voltage: {data['voltage']} V")
    print(f"Current: {data['current']} A")
    print(f"Power:   {data['power']} W")

    # 6. Show alerts instantly
    if alerts:
        print("🚨 ALERTS:")
        for a in alerts:
            print(" -", a)

    # 7. Control loop timing (important for real-time behavior)
    elapsed = time.time() - start_time
    sleep_time = max(0.5 - elapsed, 0)  # keeps stable refresh rate ~2Hz

    time.sleep(sleep_time)
