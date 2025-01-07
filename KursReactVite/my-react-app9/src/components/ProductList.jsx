import {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Search from "./Search.jsx";
import Product from "./Product.jsx";


function ProductList() {

    const [products, setProducts] = useState([]);
    const [filteredProducts, setFilteredProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            const storedProducts = localStorage.getItem("products");
            //zamiast localStorage można przekazywać propsy z rodzica
            if (storedProducts) {
                const parsedProducts = JSON.parse(storedProducts);
                setProducts(parsedProducts.products);
                setFilteredProducts(parsedProducts.products);
            } else {
                const response = await fetch("https://dummyjson.com/products");
                const data = await response.json(); //zwraca tablicę obiektów Products, ale również inne dodatkowe
                //parametry np limit, offset, total itp.
                localStorage.setItem("products", JSON.stringify(data.products));
                setProducts(data.products);
                setFilteredProducts(data.products);
            }
        };
        fetchProducts();
    }, []); //działa tylko przy pierwszym renderze

    useEffect(() => {
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
    }, [filteredProducts]);

    const handleSearch = (searchValue) => {
        const filteredProducts = products.filter(product => product.title.toLowerCase().includes(searchValue.toLowerCase()));
        setFilteredProducts(filteredProducts);
    }

    return (
        <>
            <Search onSearch={handleSearch}/>
            <div>
                {products.length > 0 ?
                    <ul>
                        {filteredProducts.map(product => (
                            <li key={product.id}>
                                <Product product={product}/>
                            </li>
                        ))}
                    </ul>
                    : <p>Brak produktów</p>}
            </div>
        </>
    );
}

export default ProductList;