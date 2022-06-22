console.log("bruh")
target = document.getElementById("id_target");
hiddenother = document.getElementById("target_other");
target.onchange = checkOther;
function checkOther(){
    console.log("bruh")
    if (target.selectedIndex == 4){
        hiddenother.style.display = "block";
    } else {
        hiddenother.style.display = "none";
    }
}
annoyingmarkers = document.querySelectorAll("marker");
for (m in annoyingmarkers){
    m.remove();
}
