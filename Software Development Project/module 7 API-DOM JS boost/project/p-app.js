const loadallpd = () => {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(data => displayProduct(data))
}

const displayProduct = (products) => {
    const productContainer = document.getElementById("product-container");

    products.forEach(product => {
        console.log(product);
        const div = document.createElement("div");
        div.classList.add("card");
        div.innerHTML = `
        <img class="card-img" src="${product.image} " alt="">
        <h5>${product.title.slice(0, 40)} </h5>
        <h3>Price: ${product.price} $</h3>
        <p>${product.description.slice(0, 60)}</p>
        <button onclick="singleProduct(${product.id})">Details</button>
        <button onclick="handleAddToCart('${product.title}', '${product.price}')">Add to Cart</button>

    `;
        productContainer.appendChild(div);
    });
}


const handleAddToCart = (name, price) => {
    const cartcount = document.getElementById("count").innerText;

    let convertedcount = parseInt(cartcount);
    convertedcount += 1;
    document.getElementById("count").innerText = convertedcount;

    const container = document.getElementById("cart-main-container");

    const div = document.createElement("div")
    div.classList.add("cart-info")
    div.innerHTML =
        `
    <p>${name.slice(0, 10)}</p>
    <h5 class="price">${price}</h5>
    `
    container.appendChild(div);
    updateTotal();
}

const updateTotal = () => {
    const allprice = document.getElementsByClassName("price");
    let count = 0;
    for (const element of allprice) {
        count = count + parseFloat(element.innerText);
    }
    document.getElementById("total").innerText = count.toFixed(2);
}


const singleProduct = (id) => {
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(res => res.json())
        .then(json => console.log(json))
}





loadallpd()