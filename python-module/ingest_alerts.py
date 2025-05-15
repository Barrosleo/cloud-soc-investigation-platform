import json
import random
from datetime import datetime, timedelta

def fetch_sample_alerts():
    # Generate simulated alert data with random severity and timestamps.
    base_time = datetime.utcnow()
    alerts = []
    for i in range(1, 6):
        alert_time = base_time - timedelta(minutes=5 * i)
        alert = {
            "alert_id": f"ALERT-{i:03d}",
            "timestamp": alert_time.isoformat() + "Z",
            "ip": f"192.168.1.{random.randint(1, 254)}",
            "severity": random.randint(1, 10)
        }
        alerts.append(alert)
    return alerts

if __name__ == "__main__":
    alerts = fetch_sample_alerts()
    print(json.dumps(alerts, indent=2))
    # Optionally, save alerts to a file
    with open("sample_data/security_alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)
