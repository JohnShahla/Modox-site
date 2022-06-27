const navMenu = document.getElementById('nav__menu'),
    navToggle = document.getElementById('nav__toggle'),
    navClose = document.getElementById('nav__close');

// Toggle Navbar
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu');
    });
}

if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    });
}


// Close Navbar After Clicking On A Link
const navLink = document.querySelectorAll('.nav__link');

navLink.forEach(n => n.addEventListener('click', () => {
    const navMenu = document.getElementById('nav__menu');
    navMenu.classList.remove('show-menu');
}));


// Accordion Skills
const skillsContent = document.getElementsByClassName('skills__content'),
    skillsHeader = document.querySelectorAll('.skills__header');

function toggleSkills() {
    let itemClass = this.parentNode.className;

    for (i = 0; i < skillsContent.length; i++) {
        skillsContent[i].className = 'skills__content skills__close';
    }

    if (itemClass === 'skills__content skills__close') {
        this.parentNode.className = 'skills__content skills__open'
    }
}

skillsHeader.forEach((el) => {
    el.addEventListener('click', toggleSkills)
});


// Qualification Tabs
const tabs = document.querySelectorAll('[data-target]'),
    tabContents = document.querySelectorAll('[data-content]');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);

        tabContents.forEach(tabContent => {
            tabContent.classList.remove('qualification__active');
        });

        target.classList.add('qualification__active');

        tabs.forEach(tab => {
            tab.classList.remove('qualification__active');
        });

        tab.classList.add('qualification__active')
    });
});


// Services Modal
const modalViews = document.querySelectorAll('.services__modal'),
    modalBtns = document.querySelectorAll('.services__button'),
    modalCloses = document.querySelectorAll('.services__modal-close');

let modal = function (modalClick) {
    modalViews[modalClick].classList.add('active-modal')
}

modalBtns.forEach((modalBtn, i) => {
    modalBtn.addEventListener('click', () => {
        modal(i)
    });
});

modalCloses.forEach((modalClose) => {
    modalClose.addEventListener('click', () => {
        modalViews.forEach(modalView => {
            modalView.classList.remove('active-modal')
        });
    });
});

// Scroll Sections Active Link
const sections = document.querySelectorAll('section[id]')

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        let sectionId = current.getAttribute('id')

        if ( sectionId.startsWith('portfolio') ) {
            let wo = document.getElementById('portfolio_web').offsetTop;
            let so = document.getElementById('portfolio_system').offsetTop + document.getElementById('portfolio_system').offsetHeight;

            if (scrollY > wo && scrollY <= so) {
                document.querySelector('.nav__menu a[href*=portfolio]').classList.add('active-link')
            } else {
                document.querySelector('.nav__menu a[href*=portfolio]').classList.remove('active-link')
            }
        } else {
            const sectionHeight = current.offsetHeight
            const sectionTop = current.offsetTop - 50;

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active-link')
            } else {
                document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active-link')
            }
        }
    })
}
window.addEventListener('scroll', scrollActive)

// Change Background Header
function scrollHeader() {
    const nav = document.getElementById('header')
    if (this.scrollY >= 80) nav.classList.add('scroll-header');
    else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

// Show Scroll Top
function scrollTop() {
    const scrollTop = document.getElementById('scroll-top');
    if (this.scrollY >= 560) {
        if (scrollTop) {
            scrollTop.classList.add('show-scroll');
        }
    } else {
        if (scrollTop) {
            scrollTop.classList.remove('show-scroll')
        }
    }
}
window.addEventListener('scroll', scrollTop)

VANTA.FOG({
    el: ".dark-theme",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    highlightColor: 0x193661,
    midtoneColor: 0xb5498,
    lowlightColor: 0xe2b57,
    baseColor: 0x0,
    blurFactor: 0.53,
    zoom: 1.50
  })