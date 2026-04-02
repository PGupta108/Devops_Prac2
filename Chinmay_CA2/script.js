function validateForm(){

let name=document.getElementById("name").value;
let email=document.getElementById("email").value;
let course=document.getElementById("course").value;
let rating=document.getElementById("rating").value;

let error=document.getElementById("error");

if(name=="" || email=="" || course=="" || rating==""){
error.innerHTML="Please fill all required fields";
return false;
}

let emailPattern=/^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

if(!email.match(emailPattern)){
error.innerHTML="Invalid email format";
return false;
}

error.innerHTML="Form submitted successfully!";
return false;

}