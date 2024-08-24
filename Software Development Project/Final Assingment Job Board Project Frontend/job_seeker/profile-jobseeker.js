document.addEventListener('DOMContentLoaded', function () {
    const token = localStorage.getItem('authToken');

    // Selecting elements
    const overviewTab = document.getElementById("overview-tab");
    const settingsTab = document.getElementById("settings-tab");
    const overviewContent = document.getElementById("overview-content");
    const settingsContent = document.getElementById("settings-content");

    // Function to show the Overview tab
    const showOverview = () => {
        overviewContent.classList.remove("hidden");
        settingsContent.classList.add("hidden");
        overviewTab.classList.add("text-indigo-600", "border-indigo-600");
        settingsTab.classList.remove("text-indigo-600", "border-indigo-600");
    };

    // Function to show the Settings tab
    const showSettings = () => {
        overviewContent.classList.add("hidden");
        settingsContent.classList.remove("hidden");
        settingsTab.classList.add("text-indigo-600", "border-indigo-600");
        overviewTab.classList.remove("text-indigo-600", "border-indigo-600");
    };

    // Event listeners for tab switching
    overviewTab.addEventListener("click", showOverview);
    settingsTab.addEventListener("click", showSettings);

    // Show the Overview tab by default on page load
    showOverview();

    if (!token) {
        alert('Unauthorized. Please log in.');
        window.location.href = '/login.html'; // Redirect to login page if unauthorized
        return;
    }

    const profileUrl = 'http://127.0.0.1:7000/job_seekers/profile/';
    const updateUrl = 'http://127.0.0.1:7000/job_seekers/profile/edit/';
    const profileElements = {
        fullName: document.getElementById('fullName'),
        username: document.getElementById('username'),  // Add username element
        about: document.getElementById('about'),
        resumeDownload: document.getElementById('resumeDownload'),
        education: document.getElementById('education'),
        experiences: document.getElementById('experiences'),
        skills: document.getElementById('skills'),
        address: document.getElementById('address'),
        country: document.getElementById('country'),
        editFirstName: document.getElementById('editFirstName'),
        editLastName: document.getElementById('editLastName'),
        editAbout: document.getElementById('editAbout'),
        editEducation: document.getElementById('editEducation'),
        editExperiences: document.getElementById('editExperiences'),
        editSkills: document.getElementById('editSkills'),
        editAddress: document.getElementById('editAddress'),
        editCountry: document.getElementById('editCountry'),
        editProfileForm: document.getElementById('editProfileForm')
    };

    async function fetchProfile() {
        try {
            const response = await fetch(profileUrl, {
                method: 'GET',
                headers: {
                    'Authorization': `Token ${token}`
                }
            });
            if (!response.ok) {
                throw new Error('Failed to fetch profile data');
            }
            const data = await response.json();
            profileElements.fullName.textContent = `${data.first_name} ${data.last_name}`;
            profileElements.username.textContent = data.user || 'No username available';  // Set username
            profileElements.about.textContent = data.about || 'No information available';
            profileElements.resumeDownload.href = data.resume || '#';
            profileElements.resumeDownload.textContent = data.resume ? 'Download Resume' : 'No Resume Available';
            profileElements.education.textContent = data.education || 'No education information available';
            profileElements.experiences.textContent = data.experiences || 'No experience information available';
            profileElements.skills.textContent = data.skills || 'No skills information available';
            profileElements.address.textContent = data.address || 'No address information available';
            profileElements.country.textContent = data.country || 'No country information available';
            
            // Populate the edit fields with existing profile data
            profileElements.editFirstName.value = data.first_name || '';
            profileElements.editLastName.value = data.last_name || '';
            profileElements.editAbout.value = data.about || '';
            profileElements.editEducation.value = data.education || '';
            profileElements.editExperiences.value = data.experiences || '';
            profileElements.editSkills.value = data.skills || '';
            profileElements.editAddress.value = data.address || '';
            profileElements.editCountry.value = data.country || '';
        } catch (error) {
            console.error('Error fetching profile:', error);
        }
    }

    async function updateProfile(data) {
        try {
            const response = await fetch(updateUrl, {
                method: 'PUT',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            if (!response.ok) {
                throw new Error('Failed to update profile');
            }
            alert('Profile updated successfully!');
        } catch (error) {
            console.error('Error updating profile:', error);
        }
    }

    profileElements.editProfileForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const profileData = {
            first_name: profileElements.editFirstName.value,
            last_name: profileElements.editLastName.value,
            about: profileElements.editAbout.value,
            education: profileElements.editEducation.value,
            experiences: profileElements.editExperiences.value,
            skills: profileElements.editSkills.value,
            address: profileElements.editAddress.value,
            country: profileElements.editCountry.value
        };
        updateProfile(profileData);
    });

    fetchProfile();
});
