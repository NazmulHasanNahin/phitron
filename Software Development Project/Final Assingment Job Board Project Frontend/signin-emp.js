document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    // Function to get the CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrfToken = getCookie('csrftoken');  // Fetch CSRF token from the cookie

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const email = document.querySelector("input[name='email']").value;
        const username = document.querySelector("input[name='username']").value;
        const password = document.querySelector("input[type='password']").value;

        try {
            const response = await fetch("http://127.0.0.1:7000/employers/auth/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,  // Include CSRF token in headers
                },
                body: JSON.stringify({
                    email: email,
                    username: username,
                    password: password,
                }),
                credentials: "include",  // Include credentials to send cookies
            });

            const data = await response.json();

            console.log("Response Data:", data);

            if (response.ok) {
                // Redirect to dashboard if login is successful
                window.location.href = "/emp-dashboard.html";
            } else {
                console.log("Login failed or session ID not found.");
            }
        } catch (error) {
            console.error('Fetch error:', error);
        }
    });
});
