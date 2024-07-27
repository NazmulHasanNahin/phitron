
const getAllUsers = () => {
    fetch('https://fakestoreapi.com/users')
        .then(res => res.json())
        .then(data => {
            // console.log(data);
            const parent = document.getElementById("all-user");
            parent.innerHTML = '';
            data.forEach(user => {
                const div = document.createElement("div");
                div.classList.add("col-md-4", "mb-4");
                div.innerHTML = `
                    <div class="card h-100">
                        <div class="card-body">
                            <h3>Id: ${user.id}</h3>
                            <h3 class="card-title ">Name: ${user.name.firstname} ${user.name.lastname}</h3>
                            <h5 class="card-title">Username: ${user.username}</h5>
                            <p class="card-text">Email: ${user.email}</p>
                            <h5 class="card-text">phone: ${user.phone}</h5>
                        </div>
                    </div>
                `;
                parent.appendChild(div);
            });
        });
};
getAllUsers();
const getUser = () => {
    const userId = document.getElementById('user-id').value;
    if (userId) {
        fetch(`https://fakestoreapi.com/users/${userId}`)
            .then(res => res.json())
            .then(user => {
                console.log(user);
                const parent = document.getElementById("user-details-container");
                parent.innerHTML = '';
                const div = document.createElement("div");
                div.classList.add("user-all");
                div.innerHTML = `
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <h3>Id: ${user.id}</h3>
                            <h3 class="card-title ">Name: ${user.name.firstname} ${user.name.lastname}</h3>
                            <h5 class="card-title">Username: ${user.username}</h5>
                            <p class="card-text">Email: ${user.email}</p>
                            <h5 class="card-text">phone: ${user.phone}</h5>
                        </div>
                    </div>
                `;
                parent.appendChild(div);
            })
            .catch(error => console.error('Error fetching user:', error));
    } else {
        alert('Please enter a user ID');
    }
};

const addUser = (event) => {
    event.preventDefault();
    const username = document.getElementById('new-username').value;
    const password = document.getElementById('new-password').value;
    const email = document.getElementById('new-email').value;

    fetch('https://fakestoreapi.com/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password,
            email
        })
    })
        .then(res => res.json())
        .then(newUser => {
            document.getElementById('status-message').textContent = 'User added successfully';
            document.getElementById('add-user-form').reset();
        });
        
};
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('add-user-form').addEventListener('submit', addUser);
});

const userLogin = (event) => {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    fetch('https://fakestoreapi.com/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        const loginStatus = document.getElementById('login-status');
        if (data.token) {
            loginStatus.textContent = 'Login successful';
        } else {
            loginStatus.textContent = 'Login failed';
        }
    })
    .catch(error => {
        console.error('Error logging in:', error);
        document.getElementById('login-status').textContent = 'Error logging in';
    });
};

document.getElementById('login-form').addEventListener('submit', userLogin);

