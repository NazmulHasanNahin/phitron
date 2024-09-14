document.addEventListener('DOMContentLoaded', function () {
    // Check if the script is running
    console.log('JavaScript Loaded');

    // Initialize Swiper
    const swiper = new Swiper('.swiper', {
        loop: true,
        autoplay: {
            delay: 3000,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    // Mobile menu functionality
    const mobileMenuButton = document.getElementById('mobileMenuButton');
    const mobileMenu = document.getElementById('mobileMenu');
    const closeMobileMenu = document.getElementById('closeMobileMenu');

    console.log('Mobile Menu Button:', mobileMenuButton);
    console.log('Mobile Menu:', mobileMenu);
    console.log('Close Mobile Menu Button:', closeMobileMenu);

    if (mobileMenuButton && mobileMenu && closeMobileMenu) {
        // Mobile menu toggle
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });

        // Close mobile menu
        closeMobileMenu.addEventListener('click', function () {
            mobileMenu.classList.add('hidden');
        });
    } else {
        console.error('One or more mobile menu elements not found in the DOM.');
    }
});
