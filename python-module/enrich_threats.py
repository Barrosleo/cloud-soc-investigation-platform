import json
import random

def enrich_alert(alert):
    # Simulate threat intelligence enrichment.
    enrichment = {
        "geo_location": "Unknown",
        "threat_level": "Low",
        "details": "No known malicious activity."
    }
    # Based on severity, adjust threat level.
    if alert.get("severity", 0) >= 8:
        enrichment["threat_level"] = "High"
        enrichment["geo_location"] = "Offshore"
        enrichment["details"] = "Observed behavior matches known threat patterns."
    elif alert.get("severity", 0) >= 5:
        enrichment["threat_level"] = "Medium"
        enrichment["geo_location"] = "Domestic"
        enrichment["details"] = "Potentially suspicious activity."
    alert.update(enrichment)
    return alert

def enrich_alerts(alerts):
    enriched = [enrich_alert(alert) for alert in alerts]
    return enriched

if __name__ == "__main__":
    # Load the sample alerts
    with open("sample_data/security_alerts.json", "r") as f:
        alerts = json.load(f)
    
    enriched_alerts = enrich_alerts(alerts)
    print(json.dumps(enriched_alerts, indent=2))
    
    # Save enriched alerts
    with open("sample_data/enriched_security_alerts.json", "w") as f:
        json.dump(enriched_alerts, f, indent=2)
