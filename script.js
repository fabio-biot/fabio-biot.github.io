/**
 * Portfolio Website - JavaScript
 * Handles interactivity, animations, and filtering
 */

// ===== DOM Content Loaded =====
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initProjectFilters();
    initScrollEffects();
    initContactForm();
    initSmoothScroll();
});

// ===== Navigation =====
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-links a');

    // Create mobile navigation
    createMobileNavigation();

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(15, 23, 42, 0.98)';
            navbar.style.backdropFilter = 'blur(15px)';
        } else {
            navbar.style.background = 'rgba(15, 23, 42, 0.9)';
            navbar.style.backdropFilter = 'blur(10px)';
        }
    });

    // Hamburger menu toggle
    hamburger.addEventListener('click', function() {
        document.querySelector('.nav-mobile').classList.add('active');
    });

    // Close mobile nav
    document.querySelector('.nav-mobile .close-btn')?.addEventListener('click', function() {
        document.querySelector('.nav-mobile').classList.remove('active');
    });

    // Close mobile nav when clicking a link
    document.querySelectorAll('.nav-mobile a').forEach(link => {
        link.addEventListener('click', function() {
            document.querySelector('.nav-mobile').classList.remove('active');
        });
    });
}

function createMobileNavigation() {
    const navLinks = document.querySelector('.nav-links');
    if (!navLinks) return;

    const mobileNav = document.createElement('div');
    mobileNav.className = 'nav-mobile';
    mobileNav.innerHTML = `
        <div class="close-btn">
            <i class="fas fa-times"></i>
        </div>
        ${Array.from(navLinks.children).map(link => link.outerHTML).join('')}
    `;
    document.body.appendChild(mobileNav);
}

// ===== Project Filters =====
function initProjectFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Update active button
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const filter = this.dataset.filter;

            // Filter projects with animation
            projectCards.forEach(card => {
                const tags = card.dataset.tags?.split(' ') || [];
                
                if (filter === 'all' || tags.includes(filter)) {
                    card.classList.remove('hidden');
                    card.style.animation = `fadeIn 0.5s ease ${Math.random() * 0.2 + 0.1}s forwards`;
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}

// ===== Scroll Effects =====
function initScrollEffects() {
    const backToTopBtn = document.getElementById('backToTop');
    const navbar = document.querySelector('.navbar');

    // Back to top button visibility
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }

        // Hide navbar on scroll down, show on scroll up
        let lastScroll = 0;
        return function() {
            const currentScroll = window.pageYOffset;
            if (currentScroll <= 0) {
                navbar.style.top = '0';
                return;
            }

            if (currentScroll > lastScroll && !navbar.classList.contains('scrolling-down')) {
                navbar.classList.add('scrolling-down');
                navbar.style.top = '-100px';
            } else if (currentScroll < lastScroll && navbar.classList.contains('scrolling-down')) {
                navbar.classList.remove('scrolling-down');
                navbar.style.top = '0';
            }
            lastScroll = currentScroll;
        };
    }());

    // Back to top click
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Animate elements on scroll
    initScrollAnimations();
}

function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                // Add staggered animation to children
                const children = entry.target.querySelectorAll('.skill-category, .project-card');
                children.forEach((child, index) => {
                    child.style.animationDelay = `${index * 0.1}s`;
                });
            }
        });
    }, observerOptions);

    // Observe sections
    document.querySelectorAll('.section-header, .skills-grid, .projects-grid').forEach(el => {
        observer.observe(el);
    });
}

// ===== Smooth Scroll =====
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Update URL hash
                history.pushState(null, null, this.getAttribute('href'));
            }
        });
    });

    // Handle hash in URL on load
    if (window.location.hash) {
        const target = document.querySelector(window.location.hash);
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    }
}

// ===== Contact Form =====
function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;

        // Show loading state
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;

        // Simulate form submission (replace with actual API call)
        try {
            // Get form data
            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            // Simulate API call delay
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Show success message
            showNotification('Message sent successfully! I\'ll get back to you soon.', 'success');
            form.reset();
        } catch (error) {
            showNotification('Something went wrong. Please try again.', 'error');
        } finally {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }
    });

    // Real-time validation
    form.querySelectorAll('input, textarea').forEach(field => {
        field.addEventListener('blur', function() {
            if (this.required && !this.value.trim()) {
                this.classList.add('error');
            } else {
                this.classList.remove('error');
            }
        });

        field.addEventListener('input', function() {
            if (this.value.trim()) {
                this.classList.remove('error');
            }
        });
    });
}

// ===== Notifications =====
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }

    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
        <span>${message}</span>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;

    document.body.appendChild(notification);

    // Remove after 4 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease forwards';
        setTimeout(() => notification.remove(), 300);
    }, 4000);

    // Add keyframes if not exists
    if (!document.querySelector('#notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes slideOut {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
            input.error, textarea.error {
                border-color: #ef4444 !important;
                box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2) !important;
            }
        `;
        document.head.appendChild(style);
    }
}

// ===== Utility Functions =====

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for performance
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ===== Keyboard Navigation =====
document.addEventListener('keydown', function(e) {
    // ESC to close mobile menu
    if (e.key === 'Escape') {
        document.querySelector('.nav-mobile.active')?.classList.remove('active');
    }
});

// ===== Parallax Effect (Optional) =====
// Uncomment to enable subtle parallax on hero section
/*
window.addEventListener('scroll', throttle(function() {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero && scrolled < window.innerHeight) {
        hero.style.backgroundPositionY = `${scrolled * 0.5}px`;
    }
}, 16));
*/

// ===== Preloader (Optional) =====
/*
window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        preloader.classList.add('fade-out');
        setTimeout(() => preloader.remove(), 500);
    }
});
*/

// ===== Console Easter Egg =====
console.log('%c👋 Hello there!', 'font-size: 24px; color: #6366f1; font-weight: bold;');
console.log('%cThanks for checking out my portfolio!', 'font-size: 14px; color: #8b5cf6;');
console.log('%cBuilt with ❤️ using HTML, CSS, and JavaScript', 'font-size: 12px; color: #94a3b8;');
