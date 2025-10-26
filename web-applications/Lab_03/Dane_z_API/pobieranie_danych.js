let products = [];

async function getData() {
    const url = "https://dummyjson.com/products";
    const response = await fetch(url);
    const data = await response.json();
    products = data.products.slice(0, 30); // Pobieramy tylko pierwsze 30 produktów
    displayProducts(products);
}

function displayProducts(products) {
    const tableBody = document.getElementById("productsBody");
    tableBody.innerHTML = '';
    const cnt = document.getElementById('cnt');
    cnt.textContent = products.length;
    products.forEach(product => {
        const row = document.createElement('tr');
        const image = document.createElement('td');
        const name = document.createElement('td');
        const description = document.createElement('td');

        const img = document.createElement('img');

        if ( product.images.length > 0) {
            img.src = product.images[0];
        } else img.src = product.images;

        img.alt =  product.title
        image.appendChild(img);
        name.textContent = product.title
        description.textContent = product.description;

        row.appendChild(img);
        row.appendChild(name);
        row.appendChild(description);

        tableBody.appendChild(row);
    })
}


function applyFilters() {
    const sortSelect = document.getElementById('sortSelect').value;
    const filterInput = document.getElementById('filterInput').value.toLowerCase();
    const cnt = document.getElementById('cnt');

    const filteredProducts = products.filter(product =>
        product.title.toLowerCase().includes(filterInput)
    );

    let sortedProducts;

    if (sortSelect === 'ascending') {
        sortedProducts = filteredProducts.sort((a, b) => a.title.localeCompare(b.title));
    } else if (sortSelect === 'descending') {
        sortedProducts = filteredProducts.sort((a, b) => b.title.localeCompare(a.title));
    } else {
        sortedProducts = filteredProducts;
    }

    cnt.textContent = sortedProducts.length;
    displayProducts(sortedProducts);
}

window.onload = getData;