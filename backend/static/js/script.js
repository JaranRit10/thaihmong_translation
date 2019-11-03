// จากรัน
// ====== หน้าต่าง navbar ===================
$('#wordBar').click(function () {
    document.getElementById("mySidenav").style.width = "250px";
})
function menubar() {
    document.getElementById("mySidenav").style.width = "250px";
}
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


$(document).ready(function () {


    $("#submitLogin").click(function () {
        console.log($("#username_login").text())
        console.log($("#password_login").text())

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
