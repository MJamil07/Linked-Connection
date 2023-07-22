const up_form = document.querySelectorAll('.up_form')


up_form[0].addEventListener('keyup' , (e)=> {
    if(up_form[0].value == 'c' || up_form[0].value == 'C') {
        up_form[1].style.display = 'none'
        up_form[2].style.display = 'none'
    }
})