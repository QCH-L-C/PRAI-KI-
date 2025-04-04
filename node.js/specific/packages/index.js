require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const WebSocket = require('ws');

const app = express();
const PORT = process.env.PORT || 3000;

// Database Connection
mongoose.connect(process.env.DB_URL, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Database connected'))
    .catch(err => console.error('Database connection error:', err));

// Routes
app.get('/', (req, res) => {
    res.send('Welcome to PRAI-KI!');
});

// WebSocket Setup
const server = app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
const wss = new WebSocket.Server({ server });

wss.on('connection', ws => {
    console.log('Client connected');
    ws.on('message', message => console.log(`Received: ${message}`));
    ws.send('Hello, Client!');
});
