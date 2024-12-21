const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const db = new sqlite3.Database('./orders.db');


db.serialize(() => {
    db.run(`
    CREATE TABLE IF NOT EXISTS orders (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER NOT NULL,
      book_id INTEGER NOT NULL,
      quantity INTEGER NOT NULL
    )
  `);
});

db.serialize(() => {
    db.run(`
    CREATE TABLE IF NOT EXISTS books (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      author TEXT NOT NULL,
      year INTEGER NOT NULL
    )
  `);

    db.run(`
    INSERT INTO books (title, author, year)
    VALUES ('Królestwo Kanciarzy', 'Leigh Bardugo', 2016),
           ('Szóstka Wron', 'Leigh Bardugo', 2015)
  `);
});

app.get('/api/orders/:user_id', (req, res) => {
    const userId = req.params.user_id;
    db.all('SELECT * FROM orders WHERE user_id = ?', [userId], (err, rows) => {
        if (err) return res.status(500).json({ error: 'Database error' });
        res.json(rows);
    });
});


app.post('/api/orders', (req, res) => {
    const { user_id, book_id, quantity } = req.body;

    if (!user_id || !book_id || !quantity) {
        return res.status(400).json({ error: 'Missing required fields' });
    }

    db.get('SELECT * FROM books WHERE id = ?', [book_id], (err, book) => {
        if (err) return res.status(500).json({ error: 'Database error' });
        if (!book) return res.status(404).json({ error: 'Book not found' });

        db.run(
            'INSERT INTO orders (user_id, book_id, quantity) VALUES (?, ?, ?)',
            [user_id, book_id, quantity],
            function (err) {
                if (err) return res.status(500).json({ error: 'Failed to create order' });
                res.status(201).json({ order_id: this.lastID });
            }
        );
    });
});

app.delete('/api/orders/:order_id', (req, res) => {
    const orderId = req.params.order_id;
    db.run('DELETE FROM orders WHERE id = ?', [orderId], function (err) {
        if (err) return res.status(500).json({ error: 'Failed to delete order' });
        if (this.changes === 0) return res.status(404).json({ error: 'Order not found' });
        res.json({ message: 'Order deleted successfully' });
    });
});

app.patch('/api/orders/:order_id', (req, res) => {
    const orderId = req.params.order_id;
    const { quantity } = req.body;

    if (!quantity) {
        return res.status(400).json({ error: 'Quantity is required' });
    }

    db.run('UPDATE orders SET quantity = ? WHERE id = ?', [quantity, orderId], function (err) {
        if (err) return res.status(500).json({ error: 'Failed to update order' });
        if (this.changes === 0) return res.status(404).json({ error: 'Order not found' });
        res.json({ message: 'Order updated successfully' });
    });
});

app.listen(4000, () => {
    console.log('Order service running on http://localhost:4000');
});

