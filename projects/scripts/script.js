
//registration forms actions
//signimg up
function signUp(){
    let create = document.getElementById("register");
    let connect = document.getElementById("connect");

    create.style.display="block";
    connect.style.display= "none";

}
//logging in
function connect(){
    let create = document.getElementById("register");
    let connect = document.getElementById("connect");

    create.style.display="none";
    connect.style.display= "block";
}