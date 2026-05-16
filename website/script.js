document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', (event) => {
    const target = anchor.getAttribute('href');
    if (!target || target === '#') return;
    const node = document.querySelector(target);
    if (!node) return;
    event.preventDefault();
    node.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });
});

const reveals = document.querySelectorAll('.reveal');
const motionReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

document.querySelectorAll('video[autoplay]').forEach((video) => {
  video.muted = true;
  video.playsInline = true;
  if (!motionReduced) {
    const play = () => video.play().catch(() => {});
    if (video.readyState >= 2) play();
    else video.addEventListener('canplay', play, { once: true });
  }
});

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.16 });
  reveals.forEach((node) => observer.observe(node));
} else {
  reveals.forEach((node) => node.classList.add('visible'));
}
