import {useEffect, useState} from "react";
import Search from "./Search.jsx";
import Product from "./Product.jsx";

function ProductList() {
    const [products, setProducts] = useState([]);
    const [filteredProducts, setFilteredProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            const storedProducts = localStorage.getItem("products");
            if (storedProducts) {
                const parsedProducts = JSON.parse(storedProducts);//to już tablica ale w formie stringa
                setProducts(parsedProducts);
                setFilteredProducts(parsedProducts);
                console.log("korzystam z danych z localStorage");
            } else {
                const response = await fetch("https://dummyjson.com/products");
                const data = await response.json();
                localStorage.setItem("products", JSON.stringify(data.products));
                setProducts(data.products); //wyjmuję z obiektu data tablicę products
                setFilteredProducts(data.products);
                console.log("korzystam z danych z API");
            }
        };

        fetchProducts();

        const timeout = setTimeout(() => {
            const productElements = document.querySelectorAll(".product-item");
            productElements.forEach((el) => {
                el.style.transition = "transform 0.5s";
                el.style.transform = "translateY(-20px)";
            });

            setTimeout(() => {
                productElements.forEach((el) => {
                    el.style.transform = "translateY(0)";
                });
            }, 500);
        }, 3000);

        return () => clearTimeout(timeout);
    }, []); //przy montowaniu komponentu


    const handleSearch = (searchValue) => {
        const filtered = products.filter(product =>
            product.title.toLowerCase().includes(searchValue.toLowerCase())
        );
        setFilteredProducts(filtered);
    };

    return (
        <>
            <Search onSearch={handleSearch}/>
            <div>
                {products.length > 0 ? (
                    <ul>
                        {filteredProducts.map(product => (
                            <li key={product.id}>
                                <Product product={product}/>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>Brak produktów</p>
                )}
            </div>
        </>
    );
}

export default ProductList;
