const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav-links');
if (toggle) toggle.addEventListener('click', () => nav.classList.toggle('open'));

document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => nav.classList.remove('open'));
});

document.querySelectorAll('[data-package]').forEach(link => {
  link.addEventListener('click', () => {
    const select = document.querySelector('select[name="package"]');
    if (select) {
      select.value = link.dataset.package;
    }
  });
});

setTimeout(() => {
  document.querySelectorAll('.flash').forEach(el => el.style.display = 'none');
}, 5000);
