fetch('http://127.0.0.1:7000/jobs/jobs/')
    .then(response => response.json())
    .then(data => {
        const jobsContainer = document.getElementById('all-jobs-container');
        jobsContainer.innerHTML = data.map(job => `
<div class="max-w-lg lg:max-w-4xl mx-auto p-4 space-y-4">
    <div class="bg-white p-4 rounded-lg shadow-md border-2 border-transparent hover:border-indigo-600 transform transition-transform duration-300 hover:-translate-y-2 hover:shadow-xl relative">
        <!-- Star Icon -->
        <div class="absolute top-0 left-0 bg-indigo-600 text-white rounded-tr-lg px-2 py-1 text-xs font-semibold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 17.75l-4.28 2.25.82-4.81-3.49-3.4 4.82-.7L12 6.75l2.13 4.29 4.82.7-3.49 3.4.82 4.81z" />
            </svg>
        </div>
        <div class="flex justify-between items-start mt-4">
            <div class="flex items-center space-x-3">
                <div>
                    <h2 class="text-lg font-semibold text-gray-800">${job.title}</h2>
                    <p class="text-sm text-gray-500">${job.company_name}</p>
                    <div class="flex items-center space-x-2 text-sm text-gray-500 mt-1 ">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5  text-indigo-600">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                            <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                        </svg>
                        <span>${job.location}</span>
                        <span class="text-gray-400">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5  text-indigo-600">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5m-9-6h.008v.008H12v-.008ZM12 15h.008v.008H12V15Zm0 2.25h.008v.008H12v-.008ZM9.75 15h.008v.008H9.75V15Zm0 2.25h.008v.008H9.75v-.008ZM7.5 15h.008v.008H7.5V15Zm0 2.25h.008v.008H7.5v-.008Zm6.75-4.5h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V15Zm0 2.25h.008v.008h-.008v-.008Zm2.25-4.5h.008v.008H16.5v-.008Zm0 2.25h.008v.008H16.5V15Z" />
                            </svg>
                        </span>
                        <span>${job.date_posted}</span>
                    </div>
                </div>
            </div>
            <div class="flex space-x-2">
                <span class="text-xs bg-green-100 text-green-700 py-1 px-2 rounded">Full Time</span>
                <span class="text-xs bg-yellow-100 text-yellow-700 py-1 px-2 rounded">Urgent</span>           
            </div>
        </div>
        <div class="flex justify-between items-center mt-2 bg-gray-50 p-2 rounded-lg">
            <p class="text-sm text-gray-600"><span class="font-semibold">Experience:</span> <span class="font-medium text-gray-800">${job.experience}</span></p>
            <a href="job-details.html?id=${job.id}" target="_blank" class="text-indigo-500 text-sm font-medium hover:underline">Apply Now</a>
        </div>
    </div>
</div>


    `).join('');
    })
    .catch(error => console.error('Error fetching jobs:', error));
