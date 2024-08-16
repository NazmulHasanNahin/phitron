document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const usernameInput = document.querySelector("input[type='text']");
  const passwordInput = document.querySelector("input[type='password']");

  form.addEventListener("submit", async function (event) {
      event.preventDefault();

      const username = usernameInput.value;
      const password = passwordInput.value;

      // Fetch CSRF token from the cookies
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

      const csrftoken = getCookie('csrftoken');

      const response = await fetch("http://127.0.0.1:7000/employers/login/", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken, // Include the CSRF token
          },
          body: JSON.stringify({
              username: username,
              password: password,
          }),
          credentials: "same-origin", 
      });

      if (response.ok) {
          const data = await response.json();
          window.location.href = "/emp-dashboard.html";
      } else {
          const errorData = await response.json();
          alert(`Login failed: ${errorData.error || "Unknown error"}`);
      }
  });
});
