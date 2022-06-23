target = document.getElementById("id_target");
hiddenother = document.getElementById("target_other");
crypto = document.getElementById("document_techinvolved_1");
cryptoamount = document.getElementById("cryptoamount");
crypto.addEventListener("click", checkCrypto);
target.onchange = checkOther;
function checkOther(){
    if (target.selectedIndex == 4){
        hiddenother.style.display = "block";
    } else {
        hiddenother.style.display = "none";
    }
}
function checkCrypto(){
    if (crypto.checked){
        cryptoamount.style.display = "block";
    } else {
        cryptoamount.style.display = "none"
    }
}
annoyingmarkers = document.querySelectorAll("marker");
for (m in annoyingmarkers){
    m.remove();
}
