import express from 'express';
import {register, login, getUserData} from '../controllers/authController.js';
import {authenticate} from "../middleware/authMiddleware.js";

const router = express.Router();

router.post('/register', register);
router.post('/login', login);
router.get('/user', authenticate, getUserData);

export default router;