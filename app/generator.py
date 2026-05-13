# app/generator.py
import random
import time

def generate_reading():
    voltage = random.uniform(210, 245)
    current = random.uniform(0.2, 12)

    power = voltage * current
    energy = power / 1000  # simplified kWh approximation

    return {
        "voltage": round(voltage, 2),
        "current": round(current, 2),
        "power": round(power, 2),
        "energy": round(energy, 4),
        "timestamp": time.time()
    }
