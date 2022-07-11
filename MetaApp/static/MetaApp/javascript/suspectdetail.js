showev = document.getElementById("showev");
showloc = document.getElementById("showloc");
evidence = document.getElementById("evidencedetails");
locations = document.getElementById("locationdetails");
evtflop = false;
loctflop = false;
showev.addEventListener("click", ShowEvidence);
showloc.addEventListener("click", ShowLocations);
function ShowEvidence(){
    if (!evtflop){
        evtflop = true;
        showev.innerText = "Hide";
        showloc.innerText = "Show";
        evidence.style.display = "grid";
        locations.style.display = "none";
    } else {
        evtflop = false;
        showev.innerText = "Show";
        showloc.innerText = "Show";
        evidence.style.display = "none";
        locations.style.display = "none";
    }
}
function ShowLocations(){
    if (!loctflop){
        loctflop = true;
        showev.innerText = "Show";
        showloc.innerText = "Hide";
        evidence.style.display = "none";
        locations.style.display = "grid";
    } else {
        loctflop = false;
        showev.innerText = "Show";
        showloc.innerText = "Show";
        evidence.style.display = "none";
        locations.style.display = "none";
    }
}