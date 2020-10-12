import { CheckRadio } from './module/payements/payements_module.js';

const name = document.getElementById('inputName')
const first_name = document.getElementById('inputFisrtName')
const address = document.getElementById('inputAddress')
const tva = document.getElementById('inputTva')
const mobile = document.getElementById('inputMobile')
const button_validate = document.getElementById('button_validate')
const price = document.getElementById('price_product')

const radio = document.querySelectorAll('.custom-control-input')

button_validate.addEventListener('click', (e) => {
    if (name.value, first_name.value, address.value, mobile.value, CheckRadio(radio).value) {
        const data = {
            "name": name.value,
            "first_name": first_name.value,
            "address": address.value,
            "mobile": mobile.value,
            "tva": tva.value,
            "price": price.textContent,
            "mehod_payement": CheckRadio(radio).value,
        }

        console.log(data)
    } else{
        console.error("SHIT !! ")
    }
})