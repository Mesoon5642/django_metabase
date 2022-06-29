target = document.getElementById("id_target");
hiddenother = document.getElementById("target_other");
crypt = document.getElementById("id_techinvolved_1");
cryptoamount = document.getElementById("cryptoamount");
target.onchange = checkOther;
function checkOther(){
    if (target.selectedIndex == 4){
        hiddenother.style.display = "block";
    } else {
        hiddenother.style.display = "none";
    }
}
function checkCrypto(){
    if (crypt.checked){
        cryptoamount.style.display = "block";
    } else {
        cryptoamount.style.display = "none"
    }
}
crypt.addEventListener("click", checkCrypto);
