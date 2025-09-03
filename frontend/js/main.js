$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});




$(document).on("click",".js-todo",function(e){
     e.preventDefault();
    $(".js-card").toggleClass("hidden")
}).on("click", ".js-button", function(e) {
    e.preventDefault();
    console.log("tap me")
   
    const $btn = $(this);
    
    // Get values
    const title = $(".js-post-title").val().trim();
    const description = $(".js-post-description").val().trim();
    const time = $(".js-post-time").val();
    const image = $(".js-post-image")[0].files[0];
    const checked = +$(".js-post-checked").prop("checked");
    
    if (!title.length) return false; // basic validation
    
    // Build FormData manually
    const formData = new FormData();
    formData.append("title", title);
    formData.append("description", description);
    formData.append("time", time);
    formData.append("checked", checked);
    if (image) formData.append("image", image);
    
    $btn.prop("disabled", 'true').text("wait a moment");
    
    $.ajax({
        type: 'POST',
        url: $(".js-post-title").data("post-url"),
        processData: false,
        contentType: false,
         
        data: formData,
       
         success:(dataHtml) =>{
            console.log("Success:", dataHtml);
            $(".js-card").addClass("hidden")
            $("#posts-container").prepend(dataHtml);
            $btn.prop("disabled",false).text("Submit");
            $(".js-post-title").val('')
            $(".js-post-description").val('')
            $(".js-post-checked").val('')
            $(".js-post-time").val('')
            $(".js-post-image").val('')


        },
        error: function(error) {
            console.warn(error);
            $btn.prop("disabled", false).text("Error");
        }
    });
});

