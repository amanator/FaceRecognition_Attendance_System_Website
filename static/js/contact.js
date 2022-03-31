// console.log('hey');

// function validateForm() {
//     let x = document.forms["myForm"]["name"].value;
//     console.log('I am in');
    
//     if (x == "") {
//       alert("Name must be filled out");
//       return false;
//     }
//   }

const name = document.getElementById('name');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
let validEmail = false;
let validPhone = false;
let validUser = false;
name.addEventListener('blur', ()=>{
  console.log("name is blurred");
  // Validate name here
  let regex = /^[a-zA-Z]([0-9a-zA-Z]){2,10}$/;
  let str = name.value;
  console.log(regex, str);
  if(regex.test(str)){
      console.log('Your name is valid');
      name.classList.remove('is-invalid');
      validUser = true;
  }
  else{
      console.log('Your name is not valid');
      name.classList.add('is-invalid');
      validUser = false;
      
  }
})

email.addEventListener('blur', ()=>{
  console.log("email is blurred");
  // Validate email here
  let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
  let str = email.value;
  console.log(regex, str);
  if(regex.test(str)){
      console.log('Your email is valid');
      email.classList.remove('is-invalid');
      validEmail = true;
  }
  else{
      console.log('Your email is not valid');
      email.classList.add('is-invalid');
      validEmail = false;
  }
})

phone.addEventListener('blur', ()=>{
  console.log("phone is blurred");
  // Validate phone here
  let regex = /^([0-9]){10}$/;
  let str = phone.value;
  console.log(regex, str);
  if(regex.test(str)){
      console.log('Your phone is valid');
      phone.classList.remove('is-invalid');
      validPhone = true;
  }
  else{
      console.log('Your phone is not valid');
      phone.classList.add('is-invalid');
      validPhone = false;
      
  }
})


  document.getElementById('btnn').addEventListener('click', (e)=>{
     if(validEmail && validPhone && validUser)
     {
      //  alert("Form is Submitted");
       document.getElementById("myfrm").submit();
      }
      else{
       alert("Invalid Entry");
     }
  })
   
