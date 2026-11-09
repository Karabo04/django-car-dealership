
const btn = document.getElementById('themeToggle');
const body = document.body;
if(localStorage.getItem('thenvalai-theme') === 'dark'){
  body.classList.add('dark');
  btn.textContent = '☀️';
}
btn.addEventListener('click', () => {
  body.classList.toggle('dark');
  const dark = body.classList.contains('dark');
  localStorage.setItem('thenvalai-theme', dark ? 'dark' : 'light');
  btn.textContent = dark ? '☀️' : '🌙';
});
