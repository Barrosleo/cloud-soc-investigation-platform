import json

def generate_report(enriched_alerts):
    report = "Security Incident Report\n"
    report += "========================\n\n"
    for alert in enriched_alerts:
        report += f"Alert ID: {alert.get('alert_id')}\n"
        report += f"Timestamp: {alert.get('timestamp')}\n"
        report += f"IP Address: {alert.get('ip')}\n"
        report += f"Severity: {alert.get('severity')}\n"
        report += f"Threat Level: {alert.get('threat_level')}\n"
        report += f"Geo-Location: {alert.get('geo_location')}\n"
        report += f"Details: {alert.get('details')}\n"
        report += "-------------------------------------\n"
    return report

if __name__ == "__main__":
    with open("sample_data/enriched_security_alerts.json", "r") as f:
        enriched_alerts = json.load(f)
    
    report = generate_report(enriched_alerts)
    print(report)
    
    # Optionally, save the report to a text file
    with open("incident_report.txt", "w") as f:
        f.write(report)
