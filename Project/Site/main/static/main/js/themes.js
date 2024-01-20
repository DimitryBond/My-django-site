let darkThemeButton = document.querySelector('.theme-button-dark');
let lightThemeButton = document.querySelector('.theme-button-light');

darkThemeButton.onclick = function () {
  document.body.classList.remove('light');
  darkThemeButton.classList.add('active');
  lightThemeButton.classList.remove('active');
};

lightThemeButton.onclick = function () {
  document.body.classList.add('light');
  lightThemeButton.classList.add('active');
  darkThemeButton.classList.remove('active');
};