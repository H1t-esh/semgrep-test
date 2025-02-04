// Vulnerable Code

// const express = require('express');
// const app = express();

// app.get('/profile', (req, res) => {
//     let username = req.query.username;  // No encoding!
//     res.send("<h1>Welcome, " + username + "</h1>");  // XSS Risk!
// });

// app.listen(3000, () => console.log('Server running on port 3000'));

//FIXED CODE:
const express = require('express');
const escapeHtml = require('escape-html');  // Output encoding

const app = express();

app.get('/profile', (req, res) => {
    let username = req.query.username || "Guest";  // Default if missing
    res.send("<h1>Welcome, " + escapeHtml(username) + "</h1>");  // Encoded output
});

app.listen(3000, () => console.log('Server running on port 3000'));

