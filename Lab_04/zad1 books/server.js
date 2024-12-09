const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');

const app = express();
const PORT = 3500;
app.use(bodyParser.json());
const db = new sqlite3.Database('./books.db', (err) => {
    if (err) {
        console.error('Nie można połączyć z bazą danych:', err.message);
    } else {
        console.log('Połączono z bazą danych SQLite.');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL)
    `, (err) => {
        if (err) {
            console.error('Nie można utworzyć tabeli:', err.message);
        } else {
            console.log('Tabela books została utworzona.');
        }
    });
});

app.get('/api/books', (req, res) => {
    db.all('SELECT * FROM books', (err, rows) => {
        if (err) {
            res.status(500).json({error: err.message});
            return;
        }
        res.json(rows);
    });
});

app.get('/api/books/:id', (req, res) => {
    const id = req.params.id;
    db.get('SELECT * FROM books WHERE id = ?', [id], (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (!row) {
            res.status(404).json({ error: 'Nie znaleziono książki o podanym ID.' });
        } else {
            res.json(row);
        }
    });
});

app.post('/api/books', (req, res) => {
    const { title, author, year } = req.body;

    if (!title || !author || !year) {
        return res.status(400).json({ error: 'Wszystkie pola (title, author, year) są wymagane.' });
    }

    db.run('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', [title, author, year],
                                                                function (err) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.status(201).json({ id: this.lastID });
        }
    });
});


app.delete('/api/books/:id', (req, res) => {
    const id = req.params.id;
    db.run('DELETE FROM books WHERE id =?', [id], (err) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json({ message: 'Książka została usunięta.' });
        }
    });
});




