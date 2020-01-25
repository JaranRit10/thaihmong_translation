// จากรัน
// ====== หน้าต่าง navbar ===================
// $('#sidebar').click(function () {
//     alert("ได้")
//     openNav()
// })
// function openNav() {
//     document.getElementById("mySidenav").style.width = "250px";
// }
// function closeNav() {
//     document.getElementById("mySidenav").style.width = "0";
// }


$(document).ready(function () {
    var init = function() {
  var shift = false;
  var caps = false;

  $(".key").mousedown(function() {
    // Setting the content to grab
    var content = $(this).html();
    var outputContent = $("#output").html();

    if (content.substr(0,4) == "<div") {
      if (shift) {
        var subDiv = $(this).find(".first-ch");
      }
      else {
        var subDiv = $(this).find(".second-ch");
      }
      content = subDiv.html();
    }

    // Setting special output, and then outputting
    if (content == "Backspace") {
      var stuff = outputContent;
      var x = stuff.length - 1;

      if (stuff.charAt(x) == ">") {
        var tagStart = stuff.lastIndexOf("<");
        $("#output").html(stuff.substr(0, tagStart));
      }
      else if (stuff.charAt(x) == ";") {
        var charStart = stuff.lastIndexOf("&");
        $("#output").html(stuff.substr(0, charStart));
      }
      else {
        $("#output").html(stuff.substr(0, x));
      }
    }
    else if (content == "Enter") {
      content = "<br />";
      $("#output").html($("#output").html() + content);
    }
    else if (content == "Tab") {
      content = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
      $("#output").html($("#output").html() + content);
    }
    else if (content == "Shift") {
      if (shift) {
        shift = false;
      }
      else {
        shift = true;
      }
    }
    else if (content == "Caps Lock") {
      if (caps) {
        caps = false;
      }
      else {
        caps = true;
      }
    }
    else if (content == "Ctrl" || content == "Alt" || content == "Win" || content == "Spl") {

    }
    else { // i.e. a letter
      capitalize = false;

      if (shift) {
        capitalize = !capitalize;
        shift = false;
      }

      if (caps) {
        capitalize = !capitalize;
      }

      if ((content.length == 1) && capitalize) {
        content = content.toUpperCase()
      }

      $("#output").html($("#output").html() + content);
    }

    outputContent = $("#output").html();

    // creating the automatic line break
    var sinceLastTag, relevantString, start, end, snippet;
    sinceLastTag = outputContent.lastIndexOf(">");
    relevantString = outputContent.substring(sinceLastTag).replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "1111");
    var relevantLength = relevantString.length;

    if (relevantLength > 1) {
	    start = relevantString.indexOf("&");
	    end = relevantString.indexOf(";") + 1;
	    snippet = relevantString.substring(start, end);
	    relevantString = relevantString.replace(snippet, "1");
    }

    if (relevantLength % 41 === 0 && relevantLength > 0) {
      var sweetSpot = outputContent.lastIndexOf(" ");
      var firstHalf = outputContent.substring(0, sweetSpot);
      var secondHalf = outputContent.substring(sweetSpot);

      $("#output").html(firstHalf + "<br />" + secondHalf);
    }
  });
};

$(document).ready(function() {
  init();
});
    // =============================
// var $keyboardWrapper = $('.virtual-keyboard'),
//     $key = $keyboardWrapper.find("input"),
//     $key_delete = $('.delete'),
//     $key_shift = $('.shift'),
//     $outputField = $('.output input'),
//     $currentValue = $outputField.val(),
//     actionKeys = $(".delete,.shift")
//     activeShiftClass = "shift-activated";
//
// // handle keystrokes
// function _keystroke(keyCase){
//
//   $key.not(actionKeys).on('click',function(e){
//     e.preventDefault();
//
//     // check for shift key for upper
//     if($key_shift.hasClass(activeShiftClass)){
//       keyCase = 'upper';
//       $key_shift.removeClass(activeShiftClass);
//     }else{
//       keyCase = 'lower';
//     }
//
//     // handle case
//     if(keyCase == 'upper'){
//       var keyValue = $(this).val().toUpperCase();
//     }else{
//       var keyValue = $(this).val().toLowerCase();
//     }
//
//     // grab current value
//     var output = $('.output input').val();
//         $outputField.val(output + keyValue);
//         getCurrentVal();
//         focusOutputField();
//   });
//
// } // keystroke
//
// // delete
// $key_delete.on('click',function(e){
//   e.preventDefault();
//   $outputField.val($currentValue.substr(0,$currentValue.length - 1));
//   getCurrentVal();
//   focusOutputField();
// });
//
// // shift
// $key_shift.on('click',function(e){
//   e.preventDefault();
//   $(this).toggleClass(activeShiftClass);
// });
//
// // grab current value of typed text
// function getCurrentVal(){
//   $currentValue = $outputField.val();
// }
//
// // focus for cursor hack
// function focusOutputField(){
//   $outputField.focus();
// }
//
// _keystroke("lower"); // init keystrokes


    //===============================
    // let Keyboard = window.SimpleKeyboard.default;
    //
    // let keyboard = new Keyboard({
    //     onChange: input => onChange(input),
    //     onKeyPress: button => onKeyPress(button)
    // });
    //
    // /**
    //  * Update simple-keyboard when input is changed directly
    //  */
    // document.querySelector(".input").addEventListener("input", event => {
    //     keyboard.setInput(event.target.value);
    // });
    //
    // console.log(keyboard);
    //
    // function onChange(input) {
    //     document.querySelector(".input").value = input;
    //     console.log("Input changed", input);
    // }
    //
    // function onKeyPress(button) {
    //     console.log("Button pressed", button);
    //
    //     /**
    //      * If you want to handle the shift and caps lock buttons
    //      */
    //     if (button === "{shift}" || button === "{lock}") handleShift();
    // }
    //
    // function handleShift() {
    //     let currentLayout = keyboard.options.layoutName;
    //     let shiftToggle = currentLayout === "default" ? "shift" : "default";
    //
    //     keyboard.setOptions({
    //         layoutName: shiftToggle
    //     });
    // }
    //=======================================
    // let Keyboard = window.SimpleKeyboard.default;
    //
    // let keyboard = new Keyboard({
    //     onChange: input => onChange(input),
    //     onKeyPress: button => onKeyPress(button)
    // });
    //
    // /**
    //  * Update simple-keyboard when input is changed directly
    //  */
    // document.querySelector(".input").addEventListener("input", event => {
    //     keyboard.setInput(event.target.value);
    // });
    //
    // console.log(keyboard);
    //
    // function onChange(input) {
    //     document.querySelector(".input").value = input;
    //     console.log("Input changed", input);
    // }
    //
    // function onKeyPress(button) {
    //     console.log("Button pressed", button);
    //
    //     /**
    //      * If you want to handle the shift and caps lock buttons
    //      */
    //     if (button === "{shift}" || button === "{lock}") handleShift();
    // }
    //
    // function handleShift() {
    //     let currentLayout = keyboard.options.layoutName;
    //     let shiftToggle = currentLayout === "default" ? "shift" : "default";
    //
    //     keyboard.setOptions({
    //         layoutName: shiftToggle
    //     });
    // }
    //=================================================
//     var simulateTyping = "Hello World!";
//     $('.keyboard')
//         .keyboard({
//             layout: 'custom',
//             customLayout: {
//                 'normal': [
//                     '` 1 2 3 4 5 6 7 8 9 0 - = {bksp}',
//                     '{tab} q w e r t y u i o p [ ] \\',
//                     'a s d f g h j k l ; \' {enter}',
//                     '{shift} z x c v b n m , . / {shift}',
//                     '{accept} {space} {left} {right}'
//                 ],
//                 'shift': [
//                     '~ ! @ # $ % ^ & * ( ) _ + {bksp}',
//                     '{tab} Q W E R T Y U I O P { } |',
//                     'A S D F G H J K L : " {enter}',
//                     '{shift} Z X C V B N M < > ? {shift}',
//                     '{accept} {space} {left} {right}'
//                 ]
//             }
//         })
//         .addTyping()
//         .addCaret({
//             caretClass: '',
//             // *** for future use ***
//             // data-attribute containing the character(s) next to the caret
//             charAttr: 'data-character',
//             // # character(s) next to the caret (can be negative for RTL)
//             // default is 1 which shows the character to the right of the caret
//             // setting this to -1 shows the character to the left
//             charIndex: -1,
//             // tweak caret position & height
//             offsetX: 0,
//             offsetY: 0,
//             adjustHt: 0
//         });
//
// // Typing Extension
//     $('.icon').click(function () {
//         var kb = $(this).prev().getkeyboard();
//         // typeIn( text, delay, callback );
//         kb.reveal().typeIn(simulateTyping, 500, function () {
//             // do something after text is added
//             // kb.accept();
//         });
//     });

    $("#submitLogin").click(function () {
        // console.log($("#username_login").text())
        // console.log($("#password_login").text())
        //
        // $.ajax({
        //     data: {
        //         username: $("#username_login").text(),
        //         password: $("#password_login").text(),
        //     },
        //     type: 'POST',
        //     url: '/checkLogin',
        //     success: (function (data) {
        //         console.log(data)
        //     }),
        //     error: function (error) {
        //         console.log(error)
        //     }
        // });
    })


//for search in admin page
    $('#wordtosearch').keydown(function () {
        setTimeout(function () {
            seachWord_Admin()
        }, 0)
    });
    $('select#select-numwordshow').change(function () {
        setTimeout(function () {
            seachWord_Admin()
        }, 0)
    });


    // for get word and gernerate table
    function seachWord_Admin() {
        $.ajax({
            data: {
                word: $('#wordtosearch').val()
            },
            type: 'POST',
            url: '/searchword',
            dataType: "json",
            success: (function (data) {
                try {
                    $("tbody.tbody_searchword").empty()
                    $("tfoot.tfoot_searchword").empty()
                    $("p#numwordshowAddmin").empty()
                    if (data.getData != "") {
                        $('#numwordshowAddmin').show()

                        var numrequest = data.getData.length;
                        var shownumword = ""
                        if (numrequest <= 100) {
                            shownumword += "มีทั้งหมด "
                            shownumword += numrequest
                            shownumword += " คำ"
                            $("p#numwordshowAddmin").append(shownumword)
                        } else {
                            shownumword += "มีมากกว่า "
                            shownumword += numrequest - 1
                            shownumword += " คำ"
                            $("p#numwordshowAddmin").append(shownumword)
                        }

                        var numlong = $('select#select-numwordshow').val()
                        // console.log(numlong)
                        if (numlong == "ทั้งหมด") {
                            numlong = data.getData.length
                            console.log(numlong)
                        }
                        i = 0;

                        for (x of data.getData) {

                            var tr = '<tr align="center" class="searchword">'
                            tr += '<td align="center" class="searchword">' + (i + 1) + '</td>'
                            tr += '<td align="center" class="searchword" id="' + "searchword_thaiword_" + x[0] + '">' + x[1] + '</td>'
                            tr += '<td align="center" class="searchword" id="' + "searchword_classword_" + x[0] + '">' + x[3] + '</td>'
                            tr += '<td align="center" class="searchword" id="' + "searchword_hmongword_" + x[0] + '">' + x[2] + '</td>'

                            // tr += '<td align="center" class="contro_searchword">' +
                            //     '<button type="button" class="btn color_button2 btn-xs" ' +
                            //     'data-toggle="modal" data-target="#editwordAdmin" id="edit_searchword" ' +
                            //     ' style="margin-right: 2px;" value="' + x[0] + '">Edit</button></td>'+
                            //     '<td align="center" class="contro_searchword">' +
                            //     '<button type="button" class="btn color_button2 btn-xs" data-toggle="modal" data-target="#deletewordModal" ' +
                            //     'id="delte_searchword" value="' + x[0] + '">Delete</button></td>'

                            tr += '<td class="contro_searchword">' +
                                '<button type="button" class="color_button2" id="edit_searchword" data-toggle="modal" data-target="#editwordAdmin" value="'+ x[0] +'">Edit</button></td>'+
                                '<td class="contro_searchword">'+
                                '<button type="button" class="color_button2" id="delte_searchword" data-toggle="modal" data-target="#deletewordModal" value="' + x[0] + '">Delete</button></td>'

                            // tr += '<td class="contro_searchword">' +
                            //     '<button type="button" class="btn color_button2 btn-xs" data-toggle="modal" data-target="#deletewordModal" ' +
                            //     'id="delte_searchword" value="' + x[0] + '">Delete</button></td>'

                            // tr += '</tr>'

                            $("tbody.tbody_searchword").append(tr)

                            if ((i + 1) >= numlong) {
                                $("tfoot.tfoot_searchword").append(
                                    '<tr class="searchword">' +
                                    '<td class="searchword" colspan="4">' + 'อีก ' + (numrequest - i - 1) + ' คำ' + '</td>' +
                                    '</tr>'
                                );
                                break;
                            }
                            i++;
                        }
                    } else {
                        $("tbody.tbody_searchword").empty()
                        $("tfoot.tfoot_searchword").empty()
                    }
                } catch (err) {
                    console.log("Error in the funtion seachWord_Admin")
                }

            }),
            error: function (error) {
                console.log(error)
            }
        });
    }

    $(this).on('click', 'button#edit_searchword', function () {
        var idword = $(this).val()
        var thaiword = $("#searchword_thaiword_" + idword).text();
        var hmongword = $('#searchword_hmongword_' + idword).text();
        var classword = $('#searchword_classword_' + idword).text();
        // 5.log(thaiword+" "+hmongword+" "+classword)
        $('input#hmongwordedit').val(hmongword)
        $('input#thaiwordEdit').val(thaiword)
        $('select#selectclassword_edit').val("NOUN")
    })

    $(this).on('click', 'button#delte_searchword', function () {
        var idword = $(this).val()
        $('#confirm_deleteword').attr("name", idword)
        var thaiword = $("#searchword_thaiword_" + idword).text();
        var hmongword = $('#searchword_hmongword_' + idword).text();
        var classword = $('#searchword_classword_' + idword).text();
        console.log(idword + " " + thaiword + " " + hmongword + " " + classword)

        $('span.wordhmongModal_delete').text(hmongword)
        $('span.wordthaiModal_delete').text(thaiword)
        $('span.classwordModal_delete').text(classword)
    })

    function insertword(userID, thaiword, hmongword, classword) {
        $.ajax({
            data: {
                userID: userID,
                thaiword: thaiword,
                hmongword: hmongword,
                classword: classword
            },
            type: 'POST',
            url: '/addnewword',
            dataType: "json",
            success: (function (data) {
                try {
                    // console.log(data.state)
                    if (data.state == true) {
                        alert("เพิ่มคำศัพท์สำเร็จ")
                    } else {
                        alert("เพิ่มคำศัพท์ผิดพลาด")
                    }
                } catch (err) {
                    alert(err)
                }
            }),
            error: function (error) {
                console.log(error)
            }
        });
    }

    function updateword(userID, idword, thaiword, hmongword, classword) {
        $.ajax({
            data: {
                idword: idword,
                userID: userID,
                thaiword: thaiword,
                hmongword: hmongword,
                classword: classword
            },
            type: 'POST',
            url: '/updateword',
            dataType: "json",
            success: (function (data) {
                if (data.state == true) {
                    alert("แก้ไขสำเร็จ")
                    seachWord_Admin()
                } else {
                    alert("แก้ไขผิดพลาด")
                }
            }),
            error: function (error) {
                console.log(error)
            }
        });
    }

    function deleteword(userID, idword, thaiword) {
        $.ajax({
            data: {
                idword: idword,
                userID: userID,
                thaiword: thaiword
            },
            type: 'POST',
            url: '/deleteword',
            dataType: "json",
            success: (function (data) {
                if (data.state == true) {
                    alert("ลบสำเร็จ")
                    seachWord_Admin()
                } else {
                    alert("ลบผิดพลาด")
                }
            }),
            error: function (error) {
                console.log(error)
            }
        });
    }


    $("#confirm_deleteword").click(function () {
        var idword = $(this).attr("name")
        var thaiword = $("#searchword_thaiword_" + idword).text();
        console.log(thaiword)
        $.ajax({
            type: 'POST',
            url: '/getdata-user',
            success: (function (data) {
                // for get user login now
                var getsession = data.dataUser[1]
                deleteword(getsession, idword, thaiword)

            }),
            error: function (error) {
                console.log(error)
            }
        });

    })

    $("button#button_addwordAdmin").click(function () {
        $('#thaiwordAdd').attr('autofocus')
    })

    // for add new word to database
    $("button#savewordadd").click(function () {
        var hmongword = $('input#hmongwordAdd').val()
        var thaiword = $('input#thaiwordAdd').val()
        var classword = $('select#selectclassword_add').val()

        if (hmongword != "" && thaiword != "" && classword != "") {
            $.ajax({
                type: 'POST',
                url: '/getdata-user',
                success: (function (data) {
                    // for get user login now
                    var getsession = data.dataUser[1]
                    // console.log(getsession)
                    // alert("test :"+getsession +" "+thaiword+" "+thaiword+" "+classword)
                    insertword(getsession, thaiword, hmongword, classword)
                    clearmodel_Addword()
                }),
                error: function (error) {
                    console.log(error)
                }
            });
        } else {
            alert("กรุณากรอกข้อมูลให้ครบด้วยครับ/ค่ะ")
        }
    });

    // for update word to database
    $("button#savewordedit").click(function () {
        var hmongword = $('input#hmongwordedit').val()
        var thaiword = $('input#thaiwordEdit').val()
        var classword = $('select#selectclassword_edit').val()
        var idword = $('button#edit_searchword').val()
        if (hmongword != "" && thaiword != "" && classword != "") {
            $.ajax({
                type: 'POST',
                url: '/getdata-user',
                success: (function (data) {
                    // for get user login now
                    var getsession = data.dataUser[1]
                    // alert("test :"+idword+" "+getsession +" "+thaiword+" "+thaiword+" "+classword)
                    updateword(getsession, idword, thaiword, hmongword, classword)
                    clearmodel_editword()
                }),
                error: function (error) {
                    console.log(error)
                }
            });
        } else {
            alert("กรุณากรอกข้อมูลให้ครบด้วยครับ/ค่ะ")
        }
    });


    // for modal addword
    $("button#clearwordadd").click(function () {
        clearmodel_Addword()
    });
    $("button#close_modal_add").click(function () {
        clearmodel_Addword()
    });

    function clearmodel_Addword() {
        $('input#hmongwordAdd').val("")
        $('input#thaiwordAdd').val("")
        $('select#selectclassword_add').val("NOUN")
    }

    // end for modal addword

    // for modal edit word
    $("button#clearwordedit").click(function () {
        clearmodel_editword()
    });
    $("button#close_modal_edit").click(function () {
        clearmodel_editword()
    });

    function clearmodel_editword() {
        $('input#hmongwordedit').val("")
        $('input#thaiwordEdit').val("")
        $('select#selectclassword_edit').val("NOUN")
    }

    // end for modal edit word


}); //end ready
