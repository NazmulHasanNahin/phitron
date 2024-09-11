// Dropdown toggles
document.getElementById('currencyDropdownButton').addEventListener('click', function () {
    document.getElementById('currencyDropdown').classList.toggle('hidden');
});

document.getElementById('languageDropdownButton').addEventListener('click', function () {
    document.getElementById('languageDropdown').classList.toggle('hidden');
});

// Mobile menu toggle
document.getElementById('mobileMenuButton').addEventListener('click', function () {
    document.getElementById('mobileMenu').classList.toggle('hidden');
});

document.getElementById('closeMobileMenu').addEventListener('click', function () {
    document.getElementById('mobileMenu').classList.add('hidden');
});

// Close dropdowns when clicking outside
document.addEventListener('click', function (e) {
    if (!e.target.closest('#currencyDropdownButton') && !e.target.closest('#currencyDropdown')) {
        document.getElementById('currencyDropdown').classList.add('hidden');
    }
    if (!e.target.closest('#languageDropdownButton') && !e.target.closest('#languageDropdown')) {
        document.getElementById('languageDropdown').classList.add('hidden');
    }
});
document.addEventListener('DOMContentLoaded', function () {
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
});



document.addEventListener('DOMContentLoaded', function () {
    const brandSwiper = new Swiper('.brand-swiper-container', {
        loop: true, // Enables infinite looping
        autoplay: {
            delay: 1300, // Autoplay delay between slides
            disableOnInteraction: false, // Autoplay continues even after interaction
        },
        pagination: {
            el: '.brand-swiper-pagination', // Pagination element
            clickable: true, // Allows pagination bullets to be clickable
        },
        navigation: {
            nextEl: '.brand-swiper-button-next', // Next button
            prevEl: '.brand-swiper-button-prev', // Previous button
        },
        slidesPerView: 4, // Shows 4 slides at a time on desktop
        spaceBetween: 10, // Space between the slides
        breakpoints: {
            // When window width is >= 320px (Mobile)
            320: {
                slidesPerView: 2, // Show 2 slides on smaller screens
                spaceBetween: 5,
            },
            // When window width is >= 640px (Tablet)
            640: {
                slidesPerView: 3, // Show 3 slides on tablets
                spaceBetween: 10,
            },
            // When window width is >= 1024px (Desktop)
            1024: {
                slidesPerView: 4, // Show 4 slides on desktop
                spaceBetween: 10,
            }
        }
    });
});
