document.addEventListener('DOMContentLoaded', () => {
  const jobsContainer = document.getElementById('jobsContainer');
  const applicationsTable = document.getElementById('applicationsTable');

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

  const sessionId = getCookie('sessionid');  // Replace with your actual cookie name

  if (!sessionId) {
      console.error('Session ID is not found. Redirecting to login.');
      window.location.href = "/signin-emp.html";
      return;
  }

  fetch('http://127.0.0.1:7000/employers/dashboard/', {
      method: 'GET',
      headers: {
          'Authorization': `Session ${sessionId}`,
          'Content-Type': 'application/json'
      },
      credentials: 'include'
  })
  .then(response => {
      console.log('Response Status:', response.status);
      if (response.status === 403) {
          console.error('Response status: 403');
          alert('Session expired or not authorized. Please log in again.');
          window.location.href = "/signin-emp.html";
          return;
      }
      return response.json();
  })
  .then(data => {
      if (data) {
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
});
