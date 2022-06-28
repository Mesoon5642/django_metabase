submit = document.getElementById("create_button")
password = document.getElementById("id_password")
conf = document.getElementById("id_confirmpassword")
warning = document.getElementById("warning")
submit.addEventListener("click", checkPasswords)
function checkPasswords(){
    if (password.value != conf.value){
        warning.style.display = "block"
    } else {
        warning.style.display = "none"
    }
}