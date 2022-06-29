showsus = document.getElementById("showsus");
suspects = document.querySelectorAll(".suspect")
showsus.addEventListener("click", ShowSuspects())
tflop = false;
function ShowSuspects(){
    if (!tflop){
        tflop = true;
        for (suspect in suspects){
            suspect.style.display = "block"
        }
    } else {
        tflop = false;
        for (suspect in suspects){
            suspect.style.display = "none"
        }
    }
}