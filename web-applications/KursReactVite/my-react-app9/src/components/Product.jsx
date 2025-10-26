import { Link } from 'react-router-dom';
import PropTypes from "prop-types";

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

Product.propTypes = {
    product: PropTypes.shape({
        id: PropTypes.number,
        title: PropTypes.string,
        category: PropTypes.string,
        brand: PropTypes.string,
    }).isRequired,
};


export default Product;