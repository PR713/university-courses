import { useParams } from "react-router-dom";

function ProductDetails() {
    const { id } = useParams();
    const storedProducts = localStorage.getItem("products");
    const products = storedProducts ? JSON.parse(storedProducts) : [];
    //samo storedProducts bo to jest string products, .products używamy gdy
    //fetchujemy dane z API i wyjmujemy tablicę products z tego obiektu data
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
