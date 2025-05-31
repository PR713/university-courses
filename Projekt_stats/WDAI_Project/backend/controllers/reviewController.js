
// backend/controllers/reviewController.js
import db from '../db/db.js';

// Pobierz opinie dla danego filmu
export const getReviews = (req, res) => {
    const { movieId } = req.params;
    db.all('SELECT * FROM reviews WHERE movieId = ?', [movieId], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
};

// Dodaj nową opinię
export const addReview = (req, res) => {
    const { movieId, name, rating, text } = req.body;
    const { userId } = req.user; // Uzyskujemy userId z req.user

    // Sprawdzamy, czy wszystkie wymagane dane zostały podane
    if (!movieId || !name || !rating || !text) {
        return res.status(400).json({ error: 'Wszystkie pola są wymagane.' });
    }

    db.all('SELECT * FROM reviews WHERE movieId = ? AND userId = ?', [movieId, userId], (err, rows) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }

        if (rows.length > 0) {
            return res.status(400).json({ error: 'Nie możesz dodać więcej niż jednej recenzji.' });
        }

        //else

        // Tworzymy datę, która będzie zapisana w recenzji
        const date = new Date().toLocaleDateString();

        // Zapytanie SQL, aby dodać nową recenzję
        const sql = 'INSERT INTO reviews (movieId, name, rating, text, date, userId) VALUES (?, ?, ?, ?, ?, ?)';
        const params = [movieId, name, rating, text, date, userId]; // Parametry dla SQL

        // Wykonanie zapytania do bazy danych
        db.run(sql, params, function (err) {
            if (err) {
                // W przypadku błędu zwracamy 500 i szczegóły błędu
                return res.status(500).json({ error: err.message });
            }

            // Zwracamy odpowiedź z id nowej recenzji
            res.json({
                id: this.lastID,
                movieId,
                name,
                rating,
                text,
                date,
                userId
            });
        });
    });
};


// Edytowanie recenzji
export const editReview = (req, res) => {
    const { reviewId } = req.params; // Id recenzji, którą chcemy edytować
    const { rating, text } = req.body; // Nowe dane recenzji


    // Sprawdzamy, czy recenzja istnieje
    db.get('SELECT * FROM reviews WHERE id = ?', [reviewId], (err, row) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }

        if (!row) {
            return res.status(404).json({ error: 'Recenzja nie została znaleziona' });
        }



        // Aktualizujemy recenzję w bazie danych
        const sql = 'UPDATE reviews SET rating = ?, text = ? WHERE id = ?';
        const params = [rating, text, reviewId];

        db.run(sql, params, function (err) {
            if (err) {
                return res.status(500).json({ error: err.message });
            }

            res.json({ message: 'Recenzja została zaktualizowana', id: reviewId });
        });
    });
};

// Usuwanie recenzji
export const deleteReview = (req, res) => {
    const { reviewId } = req.params; // Id recenzji, którą chcemy usunąć

    // Sprawdzamy, czy recenzja istnieje
    db.get('SELECT * FROM reviews WHERE id = ?', [reviewId], (err, row) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }

        if (!row) {
            return res.status(404).json({ error: 'Recenzja nie została znaleziona' });
        }



        // Usuwamy recenzję z bazy danych
        const sql = 'DELETE FROM reviews WHERE id = ?';
        const params = [reviewId];

        db.run(sql, params, function (err) {
            if (err) {
                return res.status(500).json({ error: err.message });
            }

            res.json({ message: 'Recenzja została usunięta', id: reviewId });
        });
    });
};

