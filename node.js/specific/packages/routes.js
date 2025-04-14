const express = require('express');
const router = express.Router();

router.get('/status', (req, res) => {
    res.json({ message: 'Server is running smoothly.' });
});

router.post('/data', (req, res) => {
    res.json({ message: 'Data received.' });
});

module.exports = router;
