document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const usernameInput = document.querySelector('input[type="text"]');
    const passwordInput = document.querySelector('input[type="password"]');
    const errorMessage = document.createElement('div');
  
    errorMessage.className = 'bg-white text-red-600 p-4 rounded-md mb-4';
    errorMessage.style.display = 'none';
    form.insertBefore(errorMessage, form.firstChild);
  
    const getCookie = (name) => {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    };
  
    const handleLogin = (event) => {
      event.preventDefault();
  
      const username = usernameInput.value;
      const password = passwordInput.value;
  
      if (username && password) {
        fetch('http://127.0.0.1:7000/employers/login/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password }),
        })
        .then((res) => {
          if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
          }
          return res.json();
        })
        .then((data) => {
          console.log(data);
  
          if (data.detail === 'Successfully logged in.') {
            // Store user ID and username in localStorage
            localStorage.setItem('user_id', data.user_id);  // Assuming the API returns user_id
            localStorage.setItem('username', username);
  
            // Extract session ID from cookies
            const sessionId = getCookie('sessionid'); // Ensure this matches the cookie name
  
            if (sessionId) {
              localStorage.setItem('session_id', sessionId);
              // Redirect to the profile page
              window.location.href = './emp-profile.html';
            } else {
              errorMessage.textContent = 'Session ID not found in cookies.';
              errorMessage.style.display = 'block';
            }
          } else {
            errorMessage.textContent = data.error || 'Login failed. Please try again.';
            errorMessage.style.display = 'block';
          }
        })
        .catch((error) => {
          errorMessage.textContent = `Error: ${error.message}`;
          errorMessage.style.display = 'block';
        });
      } else {
        errorMessage.textContent = 'Please enter both username and password.';
        errorMessage.style.display = 'block';
      }
    };
  
    form.addEventListener('submit', handleLogin);
  });
  