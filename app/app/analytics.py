def detect_anomalies(data):
    alerts = []

    if data["voltage"] < 200:
        alerts.append("⚠ Low Voltage Detected")

    if data["current"] > 10:
        alerts.append("⚠ High Current Load")

    if data["power"] > 2500:
        alerts.append("🔥 Power Spike Detected")

    return alerts
