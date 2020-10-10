/* active menu_mobile */

const bar_menu = document.querySelector('.bar')
bar_menu.addEventListener('click', (e) => {
    document.querySelector('.navbar_mobile').classList.remove('desactive_nav')
    document.querySelector('.navbar_mobile').classList.add('active_nav')
})

const cross_menu = document.querySelector('.cross')
cross_menu.addEventListener('click', (e) => {
    document.querySelector('.navbar_mobile').classList.remove('active_nav')
    document.querySelector('.navbar_mobile').classList.add('desactive_nav')

})