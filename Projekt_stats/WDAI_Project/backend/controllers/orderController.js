import Order from '../models/Order.js';

export const addAnOrder = async (req, res) => {
    const { userId } = req.user;
    const { address, paymentMethod, totalPrice, status, cartItems } = req.body;
    const date = new Date().toLocaleDateString();

    try {
        const orderId = await Order.addAnOrder(userId, address, paymentMethod, date, totalPrice, status, cartItems);
        res.status(201).json({ message: 'Order added', orderId });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
}

export const getOrders = async (req, res) => {
    const { userId } = req.user;

    try {
        const orders = await Order.getOrders(userId);
        res.json(orders);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
}
