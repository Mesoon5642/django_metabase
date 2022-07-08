searchbox = document.getElementById("searchbox");
searchbox.addEventListener("focus", OnFocus);
searchbox.addEventListener("focusout", OnUnfocus);
function OnFocus(){
    if (searchbox.value == "Search by Report Name..."){
        searchbox.value = "";
        searchbox.style.color = "#0B2545"
    }
}
function OnUnfocus(){
    if (searchbox.value == ""){
        searchbox.value = "Search by Report Name...";
        searchbox.style.color = "gainsboro";
        reports = document.querySelectorAll(".reportdetail");
        for (const report of reports){
            report.style.display = "block";
        }
    }
}