document.addEventListener("DOMContentLoaded", function() {
  const toggleThemeBtn = document.querySelector('.theme-toggle-btn');

  toggleThemeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-varibles');
  });
});
