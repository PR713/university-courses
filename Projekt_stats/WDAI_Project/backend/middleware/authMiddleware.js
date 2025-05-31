
import jwt from 'jsonwebtoken';

const SECRET_KEY = 'your-secret-key'; //normalnie trzymamy w np w .env

export const authenticate = (req, res, next) => {
    const token = req.header('Authorization')?.replace('Bearer ', '');

    if (!token) {
        return res.status(401).json({ error: 'Access denied. No token provided.' });
    }

    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        req.user = { userId: decoded.userId }; //można dodatkowo role,
        //bo w authController.js token też ma zaszyfrowane
        next();
    } catch (err) {
        res.status(400).json({ error: 'Invalid token.' });
    }
};

export const isAdmin = (req, res, next) => {
    if (req.user.role !== 'admin') {
        return res.status(403).json({ error: 'Access denied. Admins only.' });
    }
    next();// w sumie nieużywane bo w używamy np (/..., authenticate, editOpinion, isAdmin)
    //i isAdmin jest na końcu, można do req.user dodać przekazywanie roli, mimo że można getUserData
    //a tak to od razu w req.user.role mamy
};


