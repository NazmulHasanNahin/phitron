document.addEventListener('DOMContentLoaded', function() {
    const profileUrl = 'http://127.0.0.1:7000/employers/profile/';
    const editProfileUrl = 'http://127.0.0.1:7000/employers/profile/edit/';

    // Fetch and display user profile
    fetch(profileUrl, {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('authToken')}` // Adjust based on your auth method
        }
    })
    .then(response => response.json())
    .then(data => {
        // Populate the fields with the API data
        document.querySelector("input[name='first_name']").value = data.first_name || '';
        document.querySelector("input[name='last_name']").value = data.last_name || '';
        document.querySelector("input[name='email']").value = data.email || '';
        document.querySelector("input[name='phone']").value = data.phone || '';
        document.querySelector("input[name='address']").value = data.address || '';
        // Update other fields similarly
    })
    .catch(error => console.error('Error fetching profile data:', error));

    // Handle profile update
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        fetch(editProfileUrl, {
            method: 'PATCH',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`, // Adjust based on your auth method
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(updatedData => {
            // Handle the response after successful update
            console.log('Profile updated:', updatedData);
        })
        .catch(error => console.error('Error updating profile:', error));
    });
});
