# Cloud SOC Investigation Platform

A Cloud-Based SOC Incident Response & Investigation Platform that automates security alert ingestion, threat intelligence enrichment, incident investigation, and report generation. This project simulates real-world SOC workflows by integrating live (or sample) security alerts, enriching them with threat intelligence, and displaying findings in an interactive dashboard.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

In today’s SOC, analysts need to rapidly triage, investigate, and report on security alerts. This platform aggregates alerts, enriches them with threat intelligence, and guides the SOC analyst through a structured investigation process. The final output is a comprehensive incident report with recommendations for remediation.

## Key Features

- **Alert Ingestion & Triage:**  
  Automatically pulls security alerts (using sample data for demonstration) and prioritizes them by severity.

- **Threat Intelligence Enrichment:**  
  Simulated enrichment module that “queries” threat intelligence sources to classify IPs/domains and provide additional context.

- **Investigation Workflow:**  
  Correlates related alert data, facilitates root-cause analysis, and assigns response playbooks based on attack types.

- **Interactive Dashboard:**  
  Visualizes alert timelines, severity scores, and investigation progress using Plotly.js.

- **Automated Reporting:**  
  Generates structured incident reports including evidence, risk scores, and remediation advice.

## Architecture

For detailed information on the architecture, please refer to the [docs/architecture.md](docs/architecture.md) file.

## Technologies Used

- **Python:** Flask scripts for alert ingestion, enrichment, and report generation; libraries include pandas and requests.
- **Node.js:** Express-based API to aggregate data and serve the dashboard.
- **JavaScript/HTML:** Front-end dashboard built with Plotly.js.
- **Others:** JSON sample data, Git for version control.

## Installation & Setup

### Prerequisites

- Python 3.6+ and pip  
- Node.js (v12+ recommended)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/cloud-soc-investigation-platform.git
   cd cloud-soc-investigation-platform
   ```
2.  **Set Up the Python Module**
  ```bash
  cd python-module
  pip install -r requirements.txt
  python ingest_alerts.py
  python enrich_threats.py
  python generate_report.py
  ```
3.  **Set Up the Node.js API & Dashboard**
```bash
cd ../nodejs-api
npm install
node server.js
```
4.  **Access the Dashboard**
Open your browser at: http://localhost:3000/dashboard

## Usage

**Alert Ingestion:** The Python script ingest_alerts.py reads sample security alerts from sample_data/security_alerts.json.

**Enrichment:** The script enrich_threats.py simulates querying threat intel and combines additional context with each alert.

**Reporting:** generate_report.py produces a structured incident report (printed to console or saved as a file).

**Dashboard:** The Node.js API aggregates alert data and serves an interactive dashboard for SOC analysis.

## Project Structure
```bash
cloud-soc-investigation-platform/
├── README.md
├── docs/
│   └── architecture.md
├── python-module/
│   ├── ingest_alerts.py
│   ├── enrich_threats.py
│   ├── generate_report.py
│   ├── requirements.txt
│   └── sample_data/
│         └── security_alerts.json
├── nodejs-api/
│   ├── server.js
│   ├── package.json
│   └── views/
│         └── dashboard.html
```
## Future Enhancements
Integrate with live SIEM or cloud data sources.

Enhance threat intelligence enrichment with API calls to services like VirusTotal or MISP.

Improve automated reporting with detailed forensic analysis.

Add user authentication and role-based access to the dashboard.

## License
This project is licensed under the MIT License.
