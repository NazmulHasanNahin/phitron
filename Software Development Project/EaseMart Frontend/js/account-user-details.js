document.addEventListener('DOMContentLoaded', function () {
    // Retrieve account type and token from localStorage
    const accountType = localStorage.getItem('account_type'); // Expected values: 'customer' or 'seller'
    const token = localStorage.getItem('token');

    // Check if user is authenticated
    if (!accountType || !token) {
        showAlert('You are not authenticated. Please log in.', 'error');
        window.location.href = '/signin.html'; // Redirect to login page
        return;
    }

    // Define API endpoints based on account type
    const profileUrl = accountType === 'seller' ? 'http://127.0.0.1:7000/dashboard/profile/seller/' : 'http://127.0.0.1:7000/dashboard/profile/customer/';
    const purchasesUrl = 'http://127.0.0.1:7000/dashboard/customer/purchases/';
    const productsUrl = 'http://127.0.0.1:7000/dashboard/seller/products/';

    // Function to create alert container
    const alertContainer = document.createElement('div');
    alertContainer.id = 'alert-container';
    alertContainer.classList.add('fixed', 'top-5', 'right-5', 'z-50');
    document.body.appendChild(alertContainer);

    // Function to display a custom alert with Tailwind CSS
    function showAlert(message, type = 'error') {
        const alertContainer = document.getElementById('alert-container');

        const alertDiv = document.createElement('div');
        alertDiv.classList.add('p-4', 'rounded', 'shadow-lg', 'max-w-sm', 'mb-4', 'text-white', 'transition', 'duration-500', 'ease-in-out');

        if (type === 'error') {
            alertDiv.classList.add('bg-red-500');
        } else if (type === 'success') {
            alertDiv.classList.add('bg-green-500');
        }

        alertDiv.textContent = message;
        alertContainer.appendChild(alertDiv);

        setTimeout(() => {
            alertDiv.classList.add('opacity-0');
            setTimeout(() => alertDiv.remove(), 500);
        }, 3000);
    }

    // Function to show or hide tabs based on account type
    function setupTabs() {
        if (accountType === 'seller') {
            document.querySelector('[data-target="#productsTab"]').style.display = 'block';
            document.querySelector('[data-target="#ordersTab"]').style.display = 'none';
        } else if (accountType === 'customer') {
            document.querySelector('[data-target="#productsTab"]').style.display = 'none';
            document.querySelector('[data-target="#ordersTab"]').style.display = 'block';
        }
    }

    // Function to fetch and display account details
    function loadAccountDetails() {
        fetch(profileUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        })
            .then(async response => {
                if (response.status === 401) {
                    throw new Error('Unauthorized');
                }
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Error fetching account details');
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('first_name').value = data.first_name || '';
                document.getElementById('last_name').value = data.last_name || '';
                document.getElementById('email').value = data.email || '';
            })
            .catch(error => {
                console.error('Error fetching account details:', error);
                if (error.message === 'Unauthorized') {
                    showAlert('Session expired. Please log in again.', 'error');
                    window.location.href = '/signin.html';
                } else {
                    showAlert(`Error fetching account details: ${error.message}`, 'error');
                }
            });
    }

    // Function to handle form submission for updating account details
    const accountForm = document.getElementById('accountForm');
    accountForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const firstName = document.getElementById('first_name').value.trim();
        const lastName = document.getElementById('last_name').value.trim();
        const email = document.getElementById('email').value.trim();

        const updateData = { first_name: firstName, last_name: lastName, email: email };

        fetch(profileUrl, {
            method: 'PUT',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updateData)
        })
            .then(async response => {
                if (response.status === 401) {
                    throw new Error('Unauthorized');
                }
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Error updating account details');
                }
                return response.json();
            })
            .then(data => {
                showAlert('Account details updated successfully!', 'success');
                loadAccountDetails();
            })
            .catch(error => {
                console.error('Error updating account details:', error);
                if (error.message === 'Unauthorized') {
                    showAlert('Session expired. Please log in again.', 'error');
                    window.location.href = '/signin.html';
                } else {
                    showAlert(`Error updating account details: ${error.message}`, 'error');
                }
            });
    });

    // Function to handle logout
    const logoutBtn = document.getElementById('logoutBtn');
    logoutBtn.addEventListener('click', function () {
        // Clear token and account_type from localStorage
        localStorage.removeItem('token');
        localStorage.removeItem('account_type');
        showAlert('Logged out successfully!', 'success');

        // Redirect to login page after 1 second delay
        setTimeout(() => {
            window.location.href = '/signin.html';
        }, 1000);
    });

    // Function to fetch and display customer orders
    function fetchOrders() {
        fetch(purchasesUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        })
            .then(async response => {
                if (response.status === 401) {
                    throw new Error('Unauthorized');
                }
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Error fetching orders');
                }
                return response.json();
            })
            .then(data => {
                const ordersList = document.getElementById('ordersList');
                ordersList.innerHTML = '';
                if (data.length === 0) {
                    ordersList.innerHTML = '<li>No orders found.</li>';
                } else {
                    data.forEach(order => {
                        const orderItem = document.createElement('li');
                        orderItem.classList.add('border', 'border-gray-200', 'p-4', 'rounded-lg', 'flex', 'space-x-4');
                        orderItem.innerHTML = `
                            <img src="${order.product.image}" alt="${order.product.name}" class="w-16 h-16 object-cover rounded-md">
                            <div class="flex-1">
                                <h3 class="text-lg font-semibold">${order.product.name}</h3>
                                <p class="text-sm text-gray-600">Product ID: ${order.product.product_id}</p>
                                <p class="text-sm text-gray-600">Discounted Price: $${order.product.discounted_price}</p>
                                <p class="text-sm text-gray-600">Purchase Date: ${new Date(order.purchase_date).toLocaleDateString()}</p>
                            </div>
                        `;
                        ordersList.appendChild(orderItem);
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching orders:', error);
                if (error.message === 'Unauthorized') {
                    showAlert('Session expired. Please log in again.', 'error');
                    window.location.href = '/signin.html';
                } else {
                    showAlert(`Error fetching orders: ${error.message}`, 'error');
                }
            });
    }

    // Function to fetch and display seller products with edit/delete buttons
    function fetchSellerProducts() {
        fetch(productsUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        })
            .then(async response => {
                if (response.status === 401) {
                    throw new Error('Unauthorized');
                }
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Error fetching products');
                }
                return response.json();
            })
            .then(data => {
                const productsList = document.getElementById('productsList');
                productsList.innerHTML = '';
                if (data.length === 0) {
                    productsList.innerHTML = '<li>No products found.</li>';
                } else {
                    data.forEach(product => {
                        const productItem = document.createElement('li');
                        productItem.classList.add('border', 'border-gray-200', 'p-4', 'rounded-lg', 'mb-4');
                        productItem.innerHTML = `
                            <div class="flex items-center space-x-4">
                                <img src="${product.image}" alt="${product.name}" class="w-16 h-16 object-cover rounded-md">
                                <div>
                                    <h3 class="text-lg font-semibold">${product.name}</h3>
                                </div>
                                <div class="ml-auto">
                                    <button class="edit-product bg-blue-500 text-white px-4 py-2 rounded mr-2" data-id="${product.id}">Edit</button>
                                    <button class="delete-product bg-red-500 text-white px-4 py-2 rounded mt-4" data-id="${product.id}">Delete</button>
                                    <a href="product-details.html?id=${product.id}" class="inline-block">
                                        <button class="bg-green-500 hover:bg-green-600 text-white font-semibold px-4 py-2 rounded-lg transition duration-300 ease-in-out transform hover:scale-105 mt-4">
                                            View Details
                                        </button>
                                    </a>
                                </div>
                            </div>
                        `;
                        productsList.appendChild(productItem);
                    });

                    // Add event listeners for Edit and Delete buttons
                    document.querySelectorAll('.edit-product').forEach(button => {
                        button.addEventListener('click', function () {
                            const productId = this.getAttribute('data-id');
                            window.location.href = `/edit-product.html?id=${productId}`;
                        });
                    });

                    document.querySelectorAll('.delete-product').forEach(button => {
                        button.addEventListener('click', function () {
                            const productId = this.getAttribute('data-id');
                            deleteProduct(productId);
                        });
                    });
                }
            })
            .catch(error => {
                console.error('Error fetching products:', error);
                if (error.message === 'Unauthorized') {
                    showAlert('Session expired. Please log in again.', 'error');
                    window.location.href = '/signin.html';
                } else {
                    showAlert(`Error fetching products: ${error.message}`, 'error');
                }
            });
    }

    // Function to delete a product
    function deleteProduct(productId) {
        fetch(`http://127.0.0.1:7000/dashboard/seller/products/${productId}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        })
            .then(async response => {
                if (response.status === 401) {
                    throw new Error('Unauthorized');
                }
                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.detail || 'Error deleting product');
                }
                showAlert('Product deleted successfully!', 'success');
                fetchSellerProducts(); // Refresh the product list after deletion
            })
            .catch(error => {
                console.error('Error deleting product:', error);
                if (error.message === 'Unauthorized') {
                    showAlert('Session expired. Please log in again.', 'error');
                    window.location.href = '/signin.html';
                } else {
                    showAlert(`Error deleting product: ${error.message}`, 'error');
                }
            });
    }

    // Initialize the page based on account type
    setupTabs();
    loadAccountDetails();
    if (accountType === 'seller') {
        fetchSellerProducts();
    } else if (accountType === 'customer') {
        fetchOrders(); // Fetch orders for customer
    }
});
