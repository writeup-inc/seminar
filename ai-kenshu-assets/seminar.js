(() => {
  const header = document.getElementById('site-header');
  if (!header || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let previousY = window.scrollY;
  window.addEventListener('scroll', () => {
    const currentY = window.scrollY;
    if (currentY < 90 || currentY < previousY - 7) header.classList.remove('is-hidden');
    else if (currentY > previousY + 7) header.classList.add('is-hidden');
    previousY = currentY;
  }, { passive: true });
})();
