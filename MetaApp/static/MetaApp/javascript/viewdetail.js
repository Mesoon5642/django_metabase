showsus = document.getElementById("showsus");
showev = document.getElementById("showev");
showloc = document.getElementById("showloc");
suspects = document.getElementById("suspectdetails");
evidence = document.getElementById("evidencedetails");
locations = document.getElementById("locationdetails");
sustflop = false;
evtflop = false;
loctflop = false;
showsus.addEventListener("click", ShowSuspects);
showev.addEventListener("click", ShowEvidence);
showloc.addEventListener("click", ShowLocations);
function ShowSuspects(){
    if (!sustflop){
        sustflop = true;
        showsus.innerText = "Hide";
        showev.innerText = "Show";
        showloc.innerText = "Show";
        suspects.style.display = "block";
        evidence.style.display = "none";
        locations.style.display = "none";
    } else {
        sustflop = false;
        showsus.innerText = "Show";
        showev.innerText = "Show";
        showloc.innerText = "Show";
        suspects.style.display = "none";
        evidence.style.display = "none";
        locations.style.display = "none";
    }
}
function ShowEvidence(){
    if (!evtflop){
        evtflop = true;
        showsus.innerText = "Show";
        showev.innerText = "Hide";
        showloc.innerText = "Show";
        suspects.style.display = "none";
        evidence.style.display = "block";
        locations.style.display = "none";
    } else {
        evtflop = false;
        showsus.innerText = "Show";
        showev.innerText = "Show";
        showloc.innerText = "Show";
        suspects.style.display = "none";
        evidence.style.display = "none";
        locations.style.display = "none";
    }
}
function ShowLocations(){
    if (!loctflop){
        loctflop = true;
        showsus.innerText = "Show";
        showev.innerText = "Show";
        showloc.innerText = "Hide";
        suspects.style.display = "none";
        evidence.style.display = "none";
        locations.style.display = "block";
    } else {
        loctflop = false;
        showsus.innerText = "Show";
        showev.innerText = "Show";
        showloc.innerText = "Show";
        suspects.style.display = "none";
        evidence.style.display = "none";
        locations.style.display = "none";
    }
}