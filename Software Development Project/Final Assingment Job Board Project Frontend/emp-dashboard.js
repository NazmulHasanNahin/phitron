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
    .then(data => {
        console.log("API Response:", data);  // Log response data

        if (data) {
            const jobsContainer = document.getElementById('jobsContainer');
            const applicationsTable = document.getElementById('applicationsTable');

            // Render jobs
            data.jobs.forEach(job => {
                const jobCard = document.createElement('div');
                jobCard.className = 'bg-white shadow-md rounded-md p-4';
                jobCard.innerHTML = `
                    <h3 class="text-lg font-bold text-indigo-600">${job.title}</h3>
                    <p class="text-gray-600">${job.description}</p>
                    <p class="text-sm text-gray-500 mt-2"><strong>Location:</strong> ${job.location}</p>
                    <p class="text-sm text-gray-500"><strong>Posted On:</strong> ${job.date_posted || 'N/A'}</p>
                    <p class="text-sm text-gray-500"><strong>Salary:</strong> ${job.offer_salary}</p>
                    <p class="text-sm text-gray-500"><strong>Experience:</strong> ${job.experience}</p>
                `;
                jobsContainer.appendChild(jobCard);
            });

            // Render applications
            data.applications.forEach(application => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="px-6 py-4 whitespace-nowrap">${application.job}</td>
                    <td class="px-6 py-4 whitespace-nowrap">${application.job_seeker_name}</td>  <!-- Updated to show the job seeker name -->
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
