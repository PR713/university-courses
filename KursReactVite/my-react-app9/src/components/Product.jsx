import React from 'react';
import { Link } from 'react-router-dom';

function Product({ product }) {
    return (
        <div className="product-item">
            <Link to={`/product/${product.id}`}>
                <h3>{product.title}</h3>
                <p>Category: {product.category}</p>
                <p>Brand: {product.brand}</p>
            </Link>
        </div>
    );
}

export default Product;