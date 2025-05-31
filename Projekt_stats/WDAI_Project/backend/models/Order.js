import db from '../db/db.js';

class Order {
    static async addAnOrder(userId, address, paymentMethod, date, totalPrice, status, cartItems) {
        return new Promise((resolve,reject) => {
            db.run(
                'INSERT INTO orders (userId, address, paymentMethod, date, totalPrice, status, cartItems) VALUES (?, ?, ?, ?, ?, ?, ?)',
                [
                    userId,
                    address,
                    paymentMethod,
                    date,
                    totalPrice,
                    status,
                    JSON.stringify(cartItems)
                ],
                function(err) {
                    if (err) reject(err);
                    else resolve(this.lastID);
                }
            );
        });
    }


    static async getOrders(userId) {
        return new Promise((resolve, reject) => {
            db.all('SELECT * FROM orders WHERE userId = ?', [userId], (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
            });
        });
    }
}

export default Order;