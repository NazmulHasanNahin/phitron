const handleRegistration = (event) => {
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");

    const info = { username, first_name, last_name, email, password, confirm_password };

    document.getElementById("error").innerText = "";

    if (password !== confirm_password) {
        document.getElementById("error").innerText = "Password and confirm password do not match.";
    } else if (!/^.{8,}$/.test(password)) {
        document.getElementById("error").innerText = "Password must contain at least 8 characters.";
    } else {
        console.log(info);
        fetch("https://testing-8az5.onrender.com/patient/register/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(info)
        })
            .then(res => res.json())
            .then((data) => {
                console.log(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

}

const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
}


const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("login-username");
    const password = getValue("login-password");
    fetch("https://testing-8az5.onrender.com/patient/login/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    })
        .then(res => res.json())
        .then((data) => {
            console.log(data);
            if (data.token && data.user_id) {
                localStorage.setItem("token", data.token);
                localStorage.setItem("user_id", data.user_id);
                window.location.href="index.html";
            }
        });
}
