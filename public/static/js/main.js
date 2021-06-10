  
function alertmessage(msg_type, msg){
    $.bootstrapGrowl(msg, {
        ele: 'body', // which element to append to
        type: msg_type, // (null, 'info', 'danger', 'success')
        offset: {from: 'top', amount: 120}, // 'top', or 'bottom'
        align: 'right', // ('left', 'right', or 'center')
        width: 450, // (integer, or 'auto')
        delay: 1000, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
        allow_dismiss: true, // If true then will display a cross to close the popup.
        stackup_spacing: 10 // spacing between consecutively stacked growls.
      });

}


function login(){
    var csrf = document.getElementById('csrf').value
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    // var msg = document.getElementById('message_template')

    if(username == "" || password == ""){
    
        if(username == ""){
            document.getElementById('username_empty_msg').innerHTML = "Required";
        }
        else{
            document.getElementById('username_empty_msg').innerHTML = "";
        }
        if(password == ""){
            document.getElementById('password_empty_msg').innerHTML = "Required";
        }
        else{
            document.getElementById('password_empty_msg').innerHTML = "";
        }
    }
    else{
        var data = {
            "username" : username,
            "password" : password
        }

        fetch('/api/login/', {
            method : "POST",
            headers : {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : csrf,
            },
            body: JSON.stringify(data)
        }).then(result => result.json()).then(response => {
            if(response.status == 200){
                // alertmessage('success', response.message);
                window.location.href = '/'
                
            }
            else{
                // alert(response.message); 
                alertmessage('danger', response.message);
            }
        })


    }
}


// addimage - add blog
function defaultBtnActive(){
    const wrapper = document.querySelector(".wrapper");
    const defaultBtn = document.querySelector("#default-btn");
    const cancelBtn = document.querySelector("#cancel-btn");
    const fileName = document.querySelector(".file-name");
    const customBtn = document.querySelector("#custom-btn");
    const img = document.querySelector("#upload-img");
    let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
    defaultBtn.click();

    defaultBtn.addEventListener("change", function(){
        const file = this.files[0];
        // console.log("check file: ", file);
        if(file){
            const reader = new FileReader();
            reader.onload = function(){
                const result = reader.result;
                img.src = result;
                // console.log("img src", img.src);
                $(".imagecontainer").attr("hidden",false);
                wrapper.classList.add("active");
                $("#addimagebtn").attr("hidden",true);
            }
            cancelBtn.addEventListener("click", function(){
                img.src = "";
                wrapper.classList.remove("active");
                $(".imagecontainer").attr("hidden",true);
                $("#addimagebtn").attr("hidden",false);
            });

            reader.readAsDataURL(file);
        }
        if(this.value){
            let ValueStore = this.value.match(regExp);
            fileName.textContent = ValueStore;
        }
    });
}
