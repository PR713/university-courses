import db from '../db/db.js';

class Cart {
    static async addToCart(userId, movie) {
        return new Promise((resolve, reject) => {
            db.run(
                'INSERT INTO cart (userId, id, url, imdb_code, title, title_english, title_long, slug, year, rating, runtime, genres, summary, description_full, yt_trailer_code, language, mpa_rating, background_image, small_cover_image, medium_cover_image, large_cover_image, Director, Plot, Awards, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                [
                    userId,
                    movie.id,
                    movie.url,
                    movie.imdb_code,
                    movie.title,
                    movie.title_english,
                    movie.title_long,
                    movie.slug,
                    movie.year,
                    movie.rating,
                    movie.runtime,
                    JSON.stringify(movie.genres),
                    movie.summary,
                    movie.description_full,
                    movie.yt_trailer_code,
                    movie.language,
                    movie.mpa_rating || '',
                    movie.background_image,
                    movie.small_cover_image,
                    movie.medium_cover_image,
                    movie.large_cover_image,
                    movie.Director || 'Unknown',
                    movie.Plot || 'No description available.',
                    movie.Awards || 'N/A',
                    movie.price, // Include the price here
                ],
                function (err) {
                    if (err) reject(err);
                    else resolve(this.lastID);
                }
            );

        });
    }

    static async getCart(userId) {
        return new Promise((resolve, reject) => {
            db.all('SELECT * FROM cart WHERE userId = ?', [userId], (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
            });
        });
    }

    static async removeFromCart(userId, movieId) {
        return new Promise((resolve, reject) => {
            db.run(
                'DELETE FROM cart WHERE userId = ? AND id = ?',
                [userId, movieId],
                function (err) {
                    if (err) reject(err);
                    else resolve(this.changes);
                }
            );
        });
    }


}

export default Cart;