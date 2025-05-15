### docs/architecture.md


# Architecture & Design Overview

## System Components

1. **Python Module:**  
   - **ingest_alerts.py:** Reads security alerts (sample data) and simulates collection from SIEM/log sources.
   - **enrich_threats.py:** Simulates threat intelligence enrichment by adding context (e.g., risk scores, threat labels).
   - **generate_report.py:** Processes enriched alerts to produce a formatted incident report.

2. **Node.js API:**  
   - **server.js:** Leverages Express to serve an API endpoint to share alert data and to present a dashboard to SOC analysts.
   - **views/dashboard.html:** A user-friendly interface built with Plotly.js to visualize incident timelines and severity scores.

## Data Flow

1. **Alert Ingestion:**  
   Sample alerts (in JSON) are loaded by `ingest_alerts.py`.

2. **Threat Enrichment:**  
   Alerts are enriched with simulated threat intelligence, assigning risk based on severity.

3. **Incident Reporting:**  
   The enriched alert data is aggregated and processed to generate an incident report.

4. **Dashboard Visualization:**  
   The Node.js API accesses the enriched data (either static or dynamic) and the front-end displays an interactive timeline with meaningful annotations.

## Design Principles

- **Modularity:**  
  Each component operates independently, enabling isolated testing and incremental enhancements.

- **Scalability:**  
  The API-driven design allows integration with live data sources and expansion of enrichment capabilities.

- **User-Centric:**  
  The dashboard is designed to provide SOC analysts with clear, actionable insights at a glance.
