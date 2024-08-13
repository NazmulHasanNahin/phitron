// Toggle Mobile Menu
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Tab Switching Logic
const overviewTab = document.getElementById('overview-tab');
const settingsTab = document.getElementById('settings-tab');
const overviewContent = document.getElementById('overview-content');
const settingsContent = document.getElementById('settings-content');

overviewTab.addEventListener('click', (e) => {
    e.preventDefault();
    overviewContent.classList.remove('hidden');
    settingsContent.classList.add('hidden');
    overviewTab.classList.add('text-indigo-600', 'border-indigo-600');
    settingsTab.classList.remove('text-indigo-600', 'border-indigo-600');
});

settingsTab.addEventListener('click', (e) => {
    e.preventDefault();
    settingsContent.classList.remove('hidden');
    overviewContent.classList.add('hidden');
    settingsTab.classList.add('text-indigo-600', 'border-indigo-600');
    overviewTab.classList.remove('text-indigo-600', 'border-indigo-600');
});
