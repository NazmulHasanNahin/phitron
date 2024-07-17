const loadProducts = () => {
    fetch("https://fakestoreapi.com/products")
        .then(res => res.json())
        .then((data) => displayProducts(data))
        .catch((err) => console.log(err));
};

const displayProducts = (products) => {
    const parent = document.getElementById("products");
    parent.innerHTML = "";
    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product");
        div.innerHTML = `
            <div class="card shadow h-100">
                <div>
                    <img src="${product.image}" class="card-img-top" loading="lazy" alt="${product.title}">
                </div>
                <div class="card-body p-3 p-xl-5">
                    <h3 class="card-title h5">${product.title}</h3>
                    <p class="card-text">$${product.price}</p>
                    <a href="#" class="btn btn-primary" onclick="showProductDetails(${product.id})">Details</a>
                </div>
            </div>
        `;
        parent.appendChild(div);
    });
}

const loadCategories = () => {
    fetch("https://fakestoreapi.com/products/categories")
        .then(res => res.json())
        .then((data) => displayCategories(data))
        .catch((err) => console.log(err));
};

const displayCategories = (categories) => {
    const parent = document.getElementById("categories");
    categories.forEach(category => {
        const button = document.createElement("button");
        button.innerText = category;
        button.classList.add("btn", "btn-secondary", "m-2");
        button.addEventListener("click", () => filterProductsByCategory(category));
        parent.appendChild(button);
    });
};

const filterProductsByCategory = (category) => {
    fetch(`https://fakestoreapi.com/products/category/${category}`)
        .then(res => res.json())
        .then((data) => displayProducts(data))
        .catch((err) => console.log(err));
};

const showProductDetails = (productId) => {
    fetch(`https://fakestoreapi.com/products/${productId}`)
        .then(res => res.json())
        .then((product) => {
            const modal = document.getElementById("product-details");
            const productInfoContainer = document.getElementById("product-info");
            productInfoContainer.innerHTML = `
                <h2>${product.title}</h2>
                <img src="${product.image}" alt="${product.title}" style="width: 100px;">
                <p>${product.description}</p>
                <p>$${product.price}</p>
            `;
            modal.style.display = 'block';
        })
        .catch((err) => console.log(err));
};

const closeModal = () => {
    document.getElementById("product-details").style.display = 'none';
};

document.querySelector('.close').onclick = closeModal;
window.onclick = function(event) {
    const modal = document.getElementById("product-details");
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

loadProducts();
loadCategories();
