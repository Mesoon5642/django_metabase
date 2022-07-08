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
        reportslistjs.fuzzySearch(searchbox.value);
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