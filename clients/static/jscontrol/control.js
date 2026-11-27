document.addEventListener('DOMContentLoaded', function () {
    // Scroll reveal animation with staggered support
    const revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && revealEls.length > 0) {
        const observer = new IntersectionObserver(
            (entries, obs) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        obs.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12 }
        );
        revealEls.forEach((el) => observer.observe(el));
    } else {
        revealEls.forEach((el) => el.classList.add('is-visible'));
    }

    // Back to top button visibility & smooth scroll
    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        const toggleBackToTop = () => {
            if (window.scrollY > 240) {
                backToTop.classList.add('show');
            } else {
                backToTop.classList.remove('show');
            }
        };
        toggleBackToTop();
        window.addEventListener('scroll', toggleBackToTop);
        backToTop.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
