const dimension_form = document.getElementById('dimension')
const button_cart = document.getElementById('button_cart')
const tube_colors = document.getElementById('tube_colors')
const coating = document.getElementById('tube_colors')
const elbow_color = document.getElementById('elbow_color')
const quantities = document.getElementById('quantities')


button_cart.addEventListener('click', (e) => {
    if (dimension_form.value, tube_colors.value, coating.value, elbow_color.value, quantities.value) {
        console.log("tout à été séléctionné")
    }
})