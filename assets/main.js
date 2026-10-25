// mobile menu
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
}

// fade-in on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// gallery lightbox
const lb = document.querySelector('.lightbox');
if (lb) {
  const items = [...document.querySelectorAll('.gallery button')];
  const img = lb.querySelector('img');
  let idx = 0;
  const show = (i) => {
    idx = (i + items.length) % items.length;
    const src = items[idx].querySelector('img');
    img.src = src.src;
    img.alt = src.alt;
  };
  items.forEach((b, i) => b.addEventListener('click', () => { show(i); lb.classList.add('open'); }));
  lb.querySelector('.lb-close').addEventListener('click', () => lb.classList.remove('open'));
  lb.querySelector('.lb-next').addEventListener('click', () => show(idx + 1));
  lb.querySelector('.lb-prev').addEventListener('click', () => show(idx - 1));
  lb.addEventListener('click', (e) => { if (e.target === lb) lb.classList.remove('open'); });
  document.addEventListener('keydown', (e) => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') lb.classList.remove('open');
    if (e.key === 'ArrowLeft') show(idx + 1);
    if (e.key === 'ArrowRight') show(idx - 1);
  });
}

// contact form: no server on a static site, so open the visitor's mail app with the message
document.querySelectorAll('form.form').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const body = `שם: ${d.get('name')}\nאימייל: ${d.get('email')}\nטלפון: ${d.get('phone') || ''}\n\n${d.get('message')}`;
    const subject = `פנייה מהאתר - ${d.get('name')}`;
    window.location.href = `mailto:bekol.libi@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
});
