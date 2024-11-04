
function signUp(){
    let create = document.getElementById("register");
    let connect = document.getElementById("connect");

    create.style.display="block";
    connect.style.display= "none";

}

function connect(){
    let create = document.getElementById("register");
    let connect = document.getElementById("connect");

    create.style.display="none";
    connect.style.display= "block";
}