(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav-links');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('nav-open', open);
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); document.body.classList.remove('nav-open');
    }));
  }
  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.12, rootMargin: '0px 0px -35px 0px' });
    revealItems.forEach(item => observer.observe(item));
  } else revealItems.forEach(item => item.classList.add('is-visible'));
  const backTop = document.querySelector('.back-top');
  if (backTop) window.addEventListener('scroll', () => backTop.classList.toggle('shown', window.scrollY > 500), { passive: true });
  document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', event => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) { event.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  }));
  const params = new URLSearchParams(window.location.search);
  const product = params.get('product');
  const select = document.getElementById('id_product_interest');
  if (product && select) select.value = product;
})();
