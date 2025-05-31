import express from "express";
import {authenticate} from "../middleware/authMiddleware.js";
import {addAnOrder, getOrders} from "../controllers/orderController.js";
const router = express.Router();

router.post('/', authenticate, addAnOrder);
router.get('/userId', authenticate, getOrders);

export default router;