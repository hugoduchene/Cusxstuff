function CheckRadio(listRadio){
    let radio_checked = "";
    for (let i = 0; i < listRadio.length; i++) {
        let element = listRadio[i];
        if (element.checked) {
            radio_checked = listRadio[i]
        }
        
    }

    return radio_checked
}


export{
    CheckRadio,
}