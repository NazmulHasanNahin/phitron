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
    }
}

const getValue = (id) => {
    const value = document.getElementById(id).value;
    return value;
}