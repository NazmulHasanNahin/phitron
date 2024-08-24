const dashboard = () => {
    const token = localStorage.getItem("authToken");

    if (!token) {
        console.error("No authentication token found");
        return;
    }

    console.log("Using token:", token);  // Log the token to ensure it's correct

    fetch("http://127.0.0.1:7000/job_seekers/dashboard/", {
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
    .then(data => {
        console.log("API Response:", data);  // Log response data

        if (data) {            
            const applicationsTable = document.getElementById('applicationsTable');

            // Render applications
            data.applications.forEach(application => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="px-6 py-4 whitespace-nowrap">${application.job}</td>
                    <td class="px-6 py-4 whitespace-nowrap">${application.job_seeker}</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <a href="${application.resume}" class="text-indigo-600 hover:underline">Download</a>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">${application.cover_letter || 'N/A'}</td>
                `;
                applicationsTable.appendChild(row);
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
};

dashboard();
