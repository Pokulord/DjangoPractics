// События а документе

function DarkMode() {
    const body = document.body;
    var wasDarkMode = localStorage.getItem('darkmode') === 'true';
    localStorage.setItem('darkmode', !wasDarkMode);
    body.classList.toggle('dark_mode',!wasDarkMode);



}


document.querySelector('.switch_mode').addEventListener('click', DarkMode);


// Включаем настроенный цветовой режим при загрузке страницы


function LoadColorMode() {
    var current_theme = localStorage.getItem('darkmode');
    if (current_theme === null) {
        localStorage.setItem('darkmode',false);
    }
    document.body.classList.toggle('dark_mode', localStorage.getItem('darkmode') === 'true');
    document.querySelector('.switch_mode').checked = current_theme === 'true' ;

}


document.addEventListener('DOMContentLoaded',LoadColorMode);