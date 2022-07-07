searchbox = document.getElementById("searchbox");
searchbox.addEventListener("focus", OnFocus);
searchbox.addEventListener("focusout", OnUnfocus);
searchbox.addEventListener("keyup", SearchFunction);

function OnFocus(){
    if (searchbox.value == "Search by Report Name..."){
        searchbox.value = "";
        searchbox.style.color = "#0B2545"
    }
}
function SearchFunction(event){
    if (searchbox.value != "Search by Report Name..." && searchbox.value != "" && event.key === "Enter"){
        reports = document.querySelectorAll(".reportdetail");
        for (const report of reports){
            if (searchbox.value === report.dataset.name){
                report.style.display = "block";
            } else {
                report.style.display = "none";
            }
        }
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