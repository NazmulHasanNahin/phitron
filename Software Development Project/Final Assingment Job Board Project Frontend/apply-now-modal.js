// Get the modal element
const modal = document.getElementById('modal');
// Get the button that opens the modal
const openModalBtn = document.getElementById('openModalBtn');
// Get the button that closes the modal
const closeModalBtn = document.getElementById('closeModalBtn');

// Open the modal
openModalBtn.addEventListener('click', () => {
    modal.classList.remove('hidden');
});

// Close the modal
closeModalBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
});

// Close the modal when clicking outside of the modal content
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.classList.add('hidden');
    }
});
