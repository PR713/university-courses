import React from 'react';
import { useParams } from 'react-router-dom';

function ProductDetails() {
    const { id } = useParams();///??????????????
    const storedProducts = localStorage.getItem('products');
    const products = storedProducts ? JSON.parse(storedProducts).data : [];
    const product = products.find(p => p.id === Number(id));

    return (
        <div>
            {product ? (
                <pre>{JSON.stringify(product, null, 2)}</pre>
            ) : (
                <p>Product not found</p>
            )}
        </div>
    );
}

export default ProductDetails;