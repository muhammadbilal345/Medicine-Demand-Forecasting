function validateForm() {
    var name = document.forms["signupform"]["name"].value;
    var email = document.forms["signupform"]["email"].value;
    var password = document.forms["signupform"]["password"].value;
    var c_password = document.forms["signupform"]["c_password"].value;

    
    if (name == "") {
        alert("Please enter your name");
        return false;
    } else if (!/^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/.test(name)) {
        alert("Please enter a valid name");
        return false;
    }
    
    
    if (email == "") {
        alert("Please enter your email");
        return false;
    } else if (!/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }
    
    if (password == "") {
        alert("Please enter password");
        return false;
    } else if (!/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(password)) {
        alert("Please enter a valid password. It must be at least 8 characters long and contain at least one letter and one number.");
        return false;
    }

    if (c_password == "") {
        alert("Please enter confirm password");
        return false;
    } else if (!/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(password)) {
        alert("Please enter a valid password. It must be at least 8 characters long and contain at least one letter and one number.");
        return false;
    }

    if (password !== c_password) {
        alert("Passwords did not matched!");
        return false;
    }
    

    if (confirm("Are you sure to submit the form?")) {
        return true;
    } else {
        return false;
    }
}
