let darkThemeButton = document.querySelector('.theme-button-dark');
let lightThemeButton = document.querySelector('.theme-button-light');

darkThemeButton.onclick = function () {
  document.body.classList.remove('light');
};

lightThemeButton.onclick = function () {
  document.body.classList.add('light');
};