
// backend/routes/reviewRoutes.js
import express from 'express';
import {getReviews, addReview, editReview, deleteReview} from '../controllers/reviewController.js';
import {authenticate, isAdmin} from "../middleware/authMiddleware.js";

const router = express.Router();

// Pobierz opinie dla danego filmu
router.get('/:movieId', getReviews);

// Dodaj nową opinię
router.post('/', authenticate, addReview);

router.put('/:reviewId', authenticate, editReview, isAdmin);


router.delete('/:reviewId', authenticate, deleteReview, isAdmin);


export default router;
