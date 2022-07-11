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
susdetails = document.querySelectorAll(".susmini");
susdata = document.querySelectorAll(".susdata");
for (let i = 0; i < susdetails.length; i++){
    url = '/MetaApp/suspectdetail/' + susdata[i].textContent;
    susdetails[i].addEventListener('click', function() {
        location.href = url;
    });
}
function ShowSuspects(){
    if (!sustflop){
        sustflop = true;
        showsus.innerText = "Hide";
        showev.innerText = "Show";
        showloc.innerText = "Show";
        suspects.style.display = "grid";
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
        evidence.style.display = "grid";
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
        locations.style.display = "grid";
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