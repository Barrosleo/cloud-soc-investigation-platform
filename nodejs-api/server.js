const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files for the dashboard
app.use(express.static(path.join(__dirname, 'views')));

// API endpoint to provide enriched alert data
app.get('/api/alerts', (req, res) => {
    try {
        const alerts = require('../python-module/sample_data/enriched_security_alerts.json');
        res.json(alerts);
    } catch (error) {
        console.error("Error fetching alerts:", error);
        res.status(500).json({ error: "Failed to fetch enriched alerts." });
    }
});

app.listen(PORT, () => {
    console.log(`Node.js API running at http://localhost:${PORT}`);
});
