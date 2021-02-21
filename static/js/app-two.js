let checkBox = document.querySelector('#show-password')
checkBox.addEventListener('click', handleCheckBox, false)

function handleCheckBox(event) {
    if (this.checked) {
        password.type = 'text';
        passwordTwo.type = 'text';
    } else {
        password.type = 'password' 
        passwordTwo.type = 'password'   
    }
}

let pass1 = document.querySelector("#password");
let pass2 = document.querySelector("#passwordTwo");
let result = document.querySelector("#matching-pass");

function macthingPasswords() {
    result.innerHTML = pass1.value != pass2.value ? "Passwords Do Not Match" : "";
}

pass1.addEventListener('keyup', () => {
    if (pass2.value.length != 0) macthingPasswords()
})

pass2.addEventListener('keyup', macthingPasswords)