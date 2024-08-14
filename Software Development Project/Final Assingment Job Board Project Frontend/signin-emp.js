document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const usernameInput = document.querySelector('input[type="text"]');
    const passwordInput = document.querySelector('input[type="password"]');
    const errorMessage = document.createElement('div');
    
    errorMessage.className = 'bg-white text-red-600 p-4 rounded-md mb-4';
    errorMessage.style.display = 'none';
    form.insertBefore(errorMessage, form.firstChild);

    const handleLogin = async (event) => {
        event.preventDefault();
        
        const username = usernameInput.value;
        const password = passwordInput.value;

        console.log(username, password); // For debugging

        if (username && password) {
            try {
                const response = await fetch('http://127.0.0.1:7000/employers/login/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password }),
                });

                if (!response.ok) {
                    const data = await response.json();
                    throw new Error(data.detail || 'Login failed');
                }

                const data = await response.json();
                console.log(data); // For debugging

                if (data.token) {
                    localStorage.setItem('authToken', data.token);
                    window.location.href = './emp-profile.html';
                } else {
                    throw new Error('Invalid response format');
                }
            } catch (error) {
                errorMessage.textContent = `Error: ${error.message}`;
                errorMessage.style.display = 'block';
            }
        } else {
            errorMessage.textContent = 'Please enter both username and password.';
            errorMessage.style.display = 'block';
        }
    };

    form.addEventListener('submit', handleLogin);
});
