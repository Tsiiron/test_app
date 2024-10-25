const express = require('express');
const app = express();

app.get('/', (req, res) => {
    const name = req.query.name || 'World';
    const message = req.query.message || 'Hello';
    res.send(`Hello ${name}! ${message}!`);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running on port ${PORT}`);
});
