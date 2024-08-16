// emp-profile.js

// Function to fetch and update profile data
async function fetchAndUpdateProfile() {
  try {
      // Fetch the profile data from the API
      const response = await fetch('http://127.0.0.1:7000/employers/profile/');
      
      // Check if the request was successful
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }

      // Parse the JSON data
      const data = await response.json();

      // Update the HTML content with the fetched data
      document.querySelector('.text-xl.font-semibold.mt-4').innerHTML = data.company_name || 'N/A';
      document.querySelector('.text-indigo-600').innerHTML = data.company_description || 'N/A';
      
      // Update profile picture if available
      // Assuming the profile picture URL is stored in data.profile_picture
      // document.querySelector('.w-24.h-24.rounded-full.mx-auto').src = data.profile_picture || './image/profile.jpg';

      // Other fields that can be updated based on the API response
      // For example:
      // document.querySelector('input[type="text"][value="Jansh"]').value = data.first_name || 'N/A';
      // document.querySelector('input[type="text"][value="Dickens"]').value = data.last_name || 'N/A';
      // document.querySelector('input[type="email"][value="Jansh@gmail.com"]').value = data.email || 'N/A';
      // document.querySelector('input[type="text"][value="+2 345 678 0000"]').value = data.phone_number || 'N/A';
      // document.querySelector('input[type="text"][value="New Caledonia"]').value = data.location || 'N/A';

  } catch (error) {
      console.error('Error fetching or updating profile data:', error);
  }
}

// Call the function to fetch and update profile data when the page loads
document.addEventListener('DOMContentLoaded', fetchAndUpdateProfile);
