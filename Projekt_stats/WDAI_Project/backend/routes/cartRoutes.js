import express from 'express';
import { authenticate } from '../middleware/authMiddleware.js';
import { addToCart, getCart, removeFromCart } from '../controllers/cartController.js';

const router = express.Router();



router.post('/cart', authenticate, addToCart);
router.get('/cart', authenticate, getCart);
router.delete('/cart/:movieId', authenticate, removeFromCart);


export default router;