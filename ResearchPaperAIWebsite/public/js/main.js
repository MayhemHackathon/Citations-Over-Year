const closeButton = document.querySelector('#close-button')
const mobileButton = document.querySelector('#mobile-button')

closeButton.addEventListener('click', toggleDesktopMenu)
mobileButton.addEventListener('click', toggleDesktopMenu)

function toggleDesktopMenu() {
    document.querySelector('#desktop-panel').classList.toggle('menu-move')
}