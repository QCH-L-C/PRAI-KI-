const request = require('supertest');
const app = require('./index'); // Link to the server

test('GET /status', async () => {
    const res = await request(app).get('/status');
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe('Server is running smoothly.');
});
