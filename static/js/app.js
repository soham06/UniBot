var checkBox = document.querySelector('#show-password')
checkBox.addEventListener('click', handleCheckBox, false)

function handleCheckBox(event) {
    if (this.checked) {
        console.warn( "Change input 'type' to: text" );
        password.type = 'text';
    } else {
        console.warn( "Change input 'type' to: password" );
        password.type = 'password'   
    }
}