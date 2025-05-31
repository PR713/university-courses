import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import authRoutes from './routes/authRoutes.js';
import cartRoutes from './routes/cartRoutes.js';
import reviewRoutes from './routes/reviewRoutes.js';
import orderRoutes from "./routes/orderRoutes.js";

const app = express();
const port = 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Endpointy
app.use('/api/auth', authRoutes);
app.use('/api', cartRoutes);
app.use('/api/reviews', reviewRoutes);
app.use('/api/orders', orderRoutes);

// Uruchom serwer
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});