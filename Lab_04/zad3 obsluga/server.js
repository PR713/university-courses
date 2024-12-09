const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const sequelize = require('./sequelize');
const User = require('./user')(sequelize);

const app = express();
app.use(bodyParser.json());

const JWT_SECRET = 'supersecretkey';

app.post('/api/register', async (req, res) => {
    const { email, password } = req.body;

    try {
        const user = await User.create({ email, password });
        res.status(201).json({ id: user.id });
    } catch (error) {
        res.status(400).json({ error: 'Email is already in use or invalid data' });
    }
});

app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        const user = await User.findOne({ where: { email } });
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }


        const isMatch = await user.comparePassword(password);
        if (!isMatch) {
            return res.status(400).json({ error: 'Invalid credentials' });
        }


        const token = jwt.sign({ id: user.id }, JWT_SECRET, { expiresIn: '1h' });
        res.json({ token });
    } catch (error) {
        res.status(500).json({ error: 'Server error' });
    }
});


const authenticateJWT = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    console.log("Received token:", authHeader);

    if (!authHeader) {
        return res.status(403).json({ error: 'Access denied' });
    }

    const token = authHeader.split(' ')[1];
    if (!token) {
        return res.status(403).json({ error: 'Invalid token format' });
    }

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
            return res.status(403).json({ error: 'Invalid token' });
        }
        req.user = user;
        next();
    });
};


app.get('/api/protected', authenticateJWT, (req, res) => {
    res.json({ message: 'This is a protected route', user: req.user });
});


app.put('/api/update', authenticateJWT, async (req, res) => {
    const { email, password } = req.body;
    const userId = req.user.id;

    try {
        const user = await User.findByPk(userId);
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        user.email = email || user.email;
        user.password = password ? await bcrypt.hash(password, 10) : user.password;
        await user.save();

        res.status(200).json({ message: 'User updated successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Server error' });
    }
});


app.delete('/api/delete', authenticateJWT, async (req, res) => {
    const userId = req.user.id;
    try {
        const user = await User.findByPk(userId);
        if (!user) {
            return res.status(404).json({ error: 'User not found' });
        }

        await user.destroy();
        res.status(200).json({ message: 'User deleted successfully' });
    } catch (error) {
        res.status(500).json({ error: 'Server error' });
    }
});

sequelize.sync().then(() => {
    app.listen(4500, () => {
        console.log('Server running on http://localhost:4500');
    });
});
