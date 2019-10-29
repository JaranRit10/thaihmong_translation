
$(document).ready(function () {


    // $('#idProfile').click(function () {
    //     $.ajax({
    //         type: 'POST',
    //         url: '/getdata-user',
    //         success: (function (data) {
    //             // for get user login now
    //             var getsession = data.dataUser[1]
    //             profile(getsession)
    //             // alert("test :"+idword+" "+getsession +" "+thaiword+" "+thaiword+" "+classword)
    //
    //         }),
    //         error: function (error) {
    //             console.log(error)
    //         }
    //     })
    // })


    profile()
    function profile() {
        $.ajax({
            type : 'POST',
            url : '/getdata-user',
            success:(function(data) {
                var getUser_id = data.dataUser[1]
                console.log("getUser_id:",getUser_id)
                $.ajax({
                    type: 'POST',
                    url: '/getprofile',
                    success: (function (data) {
                        // console.log(data.getData.length)
                        var id_user
                        var username
                        var passwordd
                        var firstname
                        var lastname
                        var email
                        $("tbody#tbody_profile").empty()
                        for (x of data.getData) {
                            var id = x[0]
                            console.log("id:",id)
                            if(getUser_id == id){
                                $("td#tdUsername").append(
                                    "<h5 class='usernameRow' id='usernameRow" + x[0] + "'>" + x[3] + "</h5>"
                                );
                                // $("input#tdPassword").append(
                                //     "<p class='passwordRow' id='passwordRow"+ x[0] +"'>" + x[5] + "</p>"
                                // );
                                $("td#tdEmail").append(
                                    "<h5 class='emailRow' id='emailRow" + x[0] + "'>" + x[10] + "</h5>"
                                );
                                id_user = x[0]
                                username = x[3]
                                passwordd = x[4]
                                email = x[10]
                                // console.log("d ",passwordd)
                                firstname = x[5]
                                lastname = x[6]
                            }

                        }
                        password1(passwordd, firstname, lastname)
                        Edit_profie(username, passwordd, email, id_user)
                        save_dataProfile(username, passwordd, email, id_user)
                    }),
                    error: function (error) {
                        console.log(error)
                    }
                });
            }),
            error:function (error) {
                console.log(error)
            }
        });

        function password1(x1, x2, x3) {
            var passwords = x1
            var name = x2
            var last = x3
            console.log("x:", x)
            document.getElementById('tdPassword').value = passwords;
            document.getElementById('headName').innerText = name;
            document.getElementById('headLastname').innerText = last;
        }
        function Edit_profie(u1, u2, u3, u4) {
            var user = u1
            var pass = u2
            var email = u3
            var id_user = u4
            // $('#imag').attr('src', '/static/img/user_/'+id_user+'.jpg');
            document.getElementById('input_editusername').value = user;
            document.getElementById('input_editpassword').value = pass;
            document.getElementById('inputtd_editemail').value = email;
        }
    }

    <!-- send password -->
// function password1(x1, x2, x3) {
//     var passwords = x1
//     var name = x2
//     var last = x3
//     console.log("x:", x)
//     document.getElementById('tdPassword').value = passwords;
//     document.getElementById('headName').innerText = name;
//     document.getElementById('headLastname').innerText = last;
// }

    <!-- send edit profile -->
    function save_dataProfile(u1, u2, u3, u4) {
        var user = u1
        var pass = u2
        var email = u3
        var id_user = u4
        // document.getElementById('input_editusername').value = user;
        // document.getElementById('input_editpassword').value = pass;
        // document.getElementById('inputtd_editemail').value = email;
        // edit input
        $('#saveword_editProfile').click(function () {
            var input_user = $('input#input_editusername').val()
            var input_pass = $('input#input_editpassword').val()
            var input_email = $('input#inputtd_editemail').val()
            console.log("id_user:",id_user)
            console.log("user:",input_user)
            console.log("pass:",input_pass)
            console.log("email:",input_email)

            saveProfile()
            function saveProfile() {
                $.ajax({
                    data : {
                        id_user_ : id_user,
                        input_user_ : input_user,
                        input_pass_ : input_pass,
                        input_email_ : input_email
                    },
                    type : 'POST',
                    url : '/save_Profile',
                    success:(function(data) {
                        // alert("data:",data)
                        if (data.state == true){
                            $("td#tdUsername").empty()
                            $("input#tdPassword").empty()
                            $("td#tdEmail").empty()
                            profile()
                            alert("save success")
                        }
                        else{
                            alert(data)
                        }
                    }),
                    error:function(error) {
                        console.log(error)
                    }
                });
            }
        })
        $('#clearword_editProfile').click(function () {
            $('#input_editusername').val(" ")
            $('#input_editpassword').val(" ")
            $('#inputtd_editemail').val(" ")
        })
    }

// ================== page profile ===========================================
// $(document).ready(function () {
    function image_Page(){

    }
    $('#button_change_img').click(function () {
        changeProfile()
    })
    $('#button_edit_img').click(function () {
        removeImage()
    })

    function changeProfile() {
        $('#image').click();
    }

    $image_crop = $('#image_demo').croppie({
        enableExif: true,
        viewport: {
            width:200,
            height:200,
            type:'square' //circle
        },
        boundary:{
            width:300,
            height:300
        }
    });

    $('#image').change(function () {
        // preview_image(event)
        var imgPath = this.value;
        var ext = imgPath.substring(imgPath.lastIndexOf('.') + 1).toLowerCase();
        // var ext = imgPath.substring(imgPath.lastIndexOf(':') + 11)
        // console.log("Path img:",ext)
        // console.log("Path img1:",xx)
        if (ext == "gif" || ext == "png" || ext == "jpg" || ext == "jpeg")
            readURL(this);
        else
            alert("Please select image file (jpg, jpeg, png).")


    });

    function readURL(input) {
        if (input.files && input.files[0]) {

            // var reader = new FileReader();
            // reader.readAsDataURL(input.files[0]);
            // reader.onload = function (e) {
            //     $('#imag').attr('src', e.target.result);
            //     // $("#remove").val(0);
            //     // image on navbar
            //     $('#icon_user').attr('src', e.target.result)
            // };

            var reader = new FileReader();
            reader.onload = function (event) {
                $image_crop.croppie('bind', {
                    url: event.target.result
                }).then(function(){
                    console.log('jQuery bind complete');
                });
            }
            reader.readAsDataURL(input.files[0]);
            // $('#uploadimageModal').modal('show');
            $('#uploadimageModal').show()
        }
    }

    $('#close_model_crop').click(function () {
        $('#uploadimageModal').hide()
    })


    $('.crop_image').click(function(event){
        $image_crop.croppie('result', {
            type: 'canvas',
            size: 'viewport'
        }).then(function(response){
            $.ajax({
                type : 'POST',
                url : '/getdata-user',
                success:(function(data) {
                    var getUser_id = data.dataUser[1]
                    console.log("getUser_id:",getUser_id)

                    $.ajax({
                        url:"/crop",
                        type: "POST",
                        data:{
                            "image": response,
                            "getUser_id": getUser_id
                        },
                        success:function(data)
                        {
                            data = data.getData
                            console.log("data:",data)
                            $('#uploadimageModal').hide();
                            // $('#imag').html(data);
                            $('#imag').attr('src', data)
                        },
                        error:function (error) {
                            console.log(error)
                        }
                    });
                }),
                error:function (error) {
                    console.log(error)
                }
            });
        })
    });


    function removeImage() {
        $('#imag').attr('src', "/static/img/default_user.png");
        // $("#imag").val(1);
    }

    // function send_imag() {
    //     // var a = a
    //     // $('#imag').attr('src', "/static/img/user_/"+a);
    //     $.ajax({
    //         type : 'POST',
    //         url : '/send_imageProfile',
    //         success:(function(data) {
    //             alert("data:",data)
    //             var d = data
    //             console.log("d:",d)
    //             $('#imag').attr('src', "/static/img/user_/"+d);
    //         }),
    //         error:function(error) {
    //             console.log(error)
    //         }
    //     });
    // }
    // =================================================================

    // $("#file-picker").change(function(){
    //
    //     var input = document.getElementById('file-picker');
    //
    //     for (var i=0; i<input.files.length; i++)
    //     {
    //     //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
    //         var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()
    //
    //         if ((ext == 'jpg') || (ext == 'png'))
    //         {
    //             $("#msg").text("Files are supported")
    //         }
    //         else
    //         {
    //             $("#msg").text("Files are NOT supported")
    //             document.getElementById("file-picker").value ="";
    //         }
    //
    //     }
    //
    //
    // } );




    // $('#button_change_img').on('click', function () {
    //     var readURL = function(input) {
    //         if (input.files && input.files[0]) {
    //             var reader = new FileReader();
    //
    //             reader.onload = function (e) {
    //                 $('#imag').attr('src', e.target.result);
    //             }
    //
    //             reader.readAsDataURL(input.files[0]);
    //         }
    //     }
    //     $(".file-upload").on('change', function(){
    //         readURL(this);
    //     });
    // })



    $(function () {
        $('#imag').each(function () {
            var maxWidth = 200; // Max width for the image
            var maxHeight = 200;    // Max height for the image
            var maxratio = maxHeight / maxWidth;
            var width = $(this).width();    // Current image width
            var height = $(this).height();  // Current image height
            var curentratio = height / width;
            // Check if the current width is larger than the max

            if (curentratio > maxratio) {
                ratio = maxWidth / width;   // get ratio for scaling image
                $(this).css("width", maxWidth); // Set new width
                $(this).css("height", height * ratio); // Scale height based on ratio
            } else {
                ratio = maxHeight / height; // get ratio for scaling image
                $(this).css("height", maxHeight);   // Set new height
                $(this).css("width", width * ratio);    // Scale width based on ratio
            }
        });
    });



// ==================================================================================
//         $("#file-picker").change(function(){
//
//         var input = document.getElementById('file-picker');
//
//         for (var i=0; i<input.files.length; i++)
//         {
//         //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
//             var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()
//
//             if ((ext == 'jpg') || (ext == 'png'))
//             {
//                 $("#msg").text("Files are supported")
//             }
//             else
//             {
//                 $("#msg").text("Files are NOT supported")
//                 document.getElementById("file-picker").value ="";
//             }
//
//         }
//
//
//     } );


    // ------------- jquery sidebar -------------------------------
    // $(document).ready(function () {
    //     $('#sidebarCollapse').on('click', function () {
    //         $('#sidebar').toggleClass('active');
    //         $(this).toggleClass('active');
    //     });
    // });

// });



// ------------------- crop image -----------------------------------------------------
// $(document).ready(function(){

 // $image_crop = $('#image_demo').croppie({
 //    enableExif: true,
 //    viewport: {
 //      width:200,
 //      height:200,
 //      type:'square' //circle
 //    },
 //    boundary:{
 //      width:300,
 //      height:300
 //    }
 //  });

  // $('#upload_image').on('change', function(){
  //   var reader = new FileReader();
  //   reader.onload = function (event) {
  //     $image_crop.croppie('bind', {
  //       url: event.target.result
  //     }).then(function(){
  //       console.log('jQuery bind complete');
  //     });
  //   }
  //   reader.readAsDataURL(this.files[0]);
  //   $('#uploadimageModal').show();
  // });
  //
  //   $('.crop_image').click(function(event){
  //       $image_crop.croppie('result', {
  //           type: 'canvas',
  //           size: 'viewport'
  //       }).then(function(response){
  //       $.ajax({
  //           url:"/crop",
  //           type: "POST",
  //           data:{"image": response},
  //           success:function(data)
  //           {
  //               data = data
  //               console.log("data:",data)
  //               $('#uploadimageModal').hide();
  //               $('#uploaded_image').html(data);
  //           }
  //       });
  //   })
  // });

});


function showPassword() {
    var x = document.getElementById("tdPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}