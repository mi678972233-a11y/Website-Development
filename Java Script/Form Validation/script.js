function validate (e) {
    e.preventDefault();
    var age = document.getElementById("age").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var message = document.getElementById("message").value;
    
    let message  = " ";
    if (email === "") {
        message = "Please enter your email. ";
        msgbox.style.color = "red";
    }       
   else if (password === "") {
        message = "Please enter your password. ";
        msgbox.style.color = "red";
    }
   else if (age === "") {
        message = "Please enter your age. ";
        msgbox.style.color = "red";
    }   
   else if (message === " ") {
        message = "Login successful.";
        msgbox.style.color = "green";
    }
    msgbox.innerHTML = message;
}
// Real Time Validation When Login Is Clicked
document.getElementById("loginform").onsubmit = validate;

// Real Time Validation (Like the screenshots)
document.getElementById("email").oninput = () => validate ({preventDefault: () => {}}); 
document.getElementById("password").oninput = () => validate ({preventDefault: () => {}});
document.getElementById("age").oninput = () => validate ({preventDefault: () => {}});

