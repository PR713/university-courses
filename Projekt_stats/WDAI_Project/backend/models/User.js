import db from '../db/db.js';
import bcrypt from 'bcryptjs';

class User {
    // Tworzenie użytkownika (domyślnie jako 'user', ale można podać 'admin')
    static async create(email, password, role = 'user') {
        if (await this.findByEmail(email)) {
            throw new Error('User already exists');
        }
        const hashedPassword = await bcrypt.hash(password, 10);
        return new Promise((resolve, reject) => {
            db.run(
                'INSERT INTO users (email, password, role) VALUES (?, ?, ?)',
                [email, hashedPassword, role],
                function (err) {
                    if (err) reject(err);
                    else resolve(this.lastID);
                }
            );
        });
    }

    // Znajdowanie użytkownika po e-mailu
    static async findByEmail(email) {
        return new Promise((resolve, reject) => {
            db.get('SELECT * FROM users WHERE email = ?', [email], (err, row) => {
                if (err) reject(err);
                else resolve(row);
            });
        });
    }

    // Znajdowanie użytkownika po ID
    static async findById(id) {
        return new Promise((resolve, reject) => {
            db.get('SELECT * FROM users WHERE id = ?', [id], (err, row) => {
                if (err) reject(err);
                else resolve(row);
            });
        });
    }

    // Porównywanie haseł
    static async comparePassword(password, hashedPassword) {
        return await bcrypt.compare(password, hashedPassword);
    }



}

export default User;
