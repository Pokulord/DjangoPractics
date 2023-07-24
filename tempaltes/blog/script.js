// События а документе

function DarkMode() {
    const body = document.body;
    const wasDarkMode = localStorage.getItem('darkmode') === 'true';
    localStorage.setItem('darkmode', !wasDarkMode);

    body.classList.toggle('dark_mode',!wasDarkMode);



}


document.querySelector('.switch_mode').addEventListener('click', DarkMode);


// Включаем настроенный цветовой режим при загрузке страницы


function LoadColorMode() {
    document.body.classList.toggle('dark_mode', localStorage.getItem('darkmode') === 'true');
    document.querySelector('.switch_mode').checked = localStorage.getItem('darkmode');

}


document.addEventListener('DOMContentLoaded',LoadColorMode);