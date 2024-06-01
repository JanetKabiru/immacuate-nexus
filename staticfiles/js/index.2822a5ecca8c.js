const navLinks = document.querySelectorAll('.nav-link');

// Iterate over each element and remove the 'active' class
navLinks.forEach(link => {    
    link.classList.remove('active');
    console.log("execute");
});

if(window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    var csrftoken = getCookie('csrftoken');
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var $myForm = $('.contact-form')
    $myForm.submit(function(event){
        event.preventDefault();
        console.log("Sending");
        // grecaptcha.ready(function(){
        //     grecaptcha.execute(recaptcha_site_key, {action:"/contact"}).then(function(token){                
        //         document.getElementById('id_token').value = token;

                var $formData = $myForm.serialize();
                var $thisURL = $myForm.attr('data-url');
                $.ajax({
                    method: "POST",
                    url: $thisURL,
                    data: $formData,
                    success: handleFormSuccess,
                    error: handleFormError,
                });
        //     });
        // });                
    })

    function handleFormSuccess(data, textStatus, jqXHR){
        
        if(textStatus === 'success') {            
            var mes = "Your message has been received. We will reach out shortly";                        
            Swal.fire({
              title: 'Sent!',
              text: mes,
              icon: 'success',
              showCloseButton: true,                  
              showClass: {
                popup: 'animate__animated animate__fadeInDown'
              },
              hideClass: {
                popup: 'animate__animated animate__fadeOutUp'
              },
              background: '#fff',
              backdrop: `rgba(142, 36, 36, 0.239)`
            })               

        } else {
            var mes = "Unexpected error occured. Kindly try again";                            
            Swal.fire({
              title: 'Error Sending!',
              text: mes,
              icon: 'error',
              showCloseButton: true,                  
              showClass: {
                popup: 'animate__animated animate__fadeInDown'
              },
              hideClass: {
                popup: 'animate__animated animate__fadeOutUp'
              },
              background: '#fff',
              backdrop: `rgba(142, 36, 36, 0.239)`
            })               
        }
        
        
        $myForm[0].reset(); 
    }

    function handleFormError(jqXHR, textStatus, errorThrown){        
        // if(textStatus === 'error') {
        //     var mes = "Unexpected error occured. Kindly try again";                        
        //     Swal.fire({
        //       title: 'Error Sending!',
        //       text: mes,
        //       icon: 'error',
        //       showCloseButton: true,                  
        //       showClass: {
        //         popup: 'animate__animated animate__fadeInDown'
        //       },
        //       hideClass: {
        //         popup: 'animate__animated animate__fadeOutUp'
        //       },
        //       background: '#fff url(https://static.wixstatic.com/media/5498a7_1dbaf80a4d0a4ddcba0bdf398c8688a5~mv2.png)',
        //       backdrop: `
        //         rgba(0, 45, 64, 0.769)
        //         url("https://static.wixstatic.com/media/5498a7_1dbaf80a4d0a4ddcba0bdf398c8688a5~mv2.png")
        //         center
        //         no-repeat
        //       `
        //     })               
        // }
    }   
})