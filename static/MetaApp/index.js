login = document.getElementById("login");
logout = document.getElementById("logout");
logout.addEventListener("click", Logout);
username = getCookie("LOGGED_USERNAME");
if (username != ""){
    login.innerText = "Hello, " + username;
    login.href = "javascript:void(0)";
    login.style.cursor = "default";
    logout.style.display = "block";
}
function Logout(){
    login.innerText = "Login";
    login.href = "/MetaApp/login";
    login.style.cursor = "pointer";
    logout.style.display = "none";
    setCookie("LOGGED_USERNAME", "", 1);
    setCookie("LOGGED_REALNAME", "", 1);
}