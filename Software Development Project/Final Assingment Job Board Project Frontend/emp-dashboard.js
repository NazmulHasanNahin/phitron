const dashboard = () => {
    const token = localStorage.getItem("authToken");

    if (!token) {
        console.error("No authentication token found");
        return;
    }

    console.log("Using token:", token);  // Log the token to ensure it's correct

    fetch("http://127.0.0.1:7000/employers/dashboard/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${token}`  // Ensure correct format
        }
    })
    .then((res) => {
        console.log("Response status:", res.status);  // Log response status
        return res.json();
    })
    .then((data) => {
        console.log("API Response:", data);  // Log response data
    })
    .catch((err) => console.error("Fetch error:", err));
};

dashboard();
