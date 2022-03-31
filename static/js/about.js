console.log('This is about');
v = document.getElementById('txt');


$(document).ready(function () {
    
    $("#test").submit(function (event) {
    
      $.ajax({
        type: "POST",
        url: '/info/about/',
        encode: true,
        data: {
          'video':v.value // from form
        },
        success: function (data) {
           console.log(data);
           
          console.log('got it back');
        }
      });
      return false; //<---- move it here
    });
  
  });