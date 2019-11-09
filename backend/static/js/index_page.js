$(document).ready(function () {

    $('#clear_textarea').click(function () {
        $('textarea#thaiword').val("")
        translate2()
    })


    $('#copy_button').click(function () {
        copy()
    })
    function copy() {
        let textarea = document.getElementById("get_textarea");
        // console.log("tex:",textarea)
        textarea.select();
        document.execCommand("copy");
    }


    showTime()
    function showTime() {
        try {
            var clockElement = document.getElementById("clock");

            function updateClock(clock) {
                clock.innerHTML = new Date().toLocaleTimeString();
            }

            setInterval(function () {
                updateClock(clockElement);
            }, 1000);
        } catch (e) {

        }
    }

    //get word where selected
    function get_selection() {
        var txt = '';
        if (window.getSelection) {
            txt = window.getSelection().toString();
            seachWord(txt)
        } else if (document.selection) {
            txt = document.selection.createRange().text;
        }
        // document.getElementById("wordselect").innerHTML = txt;
    }

    $("#thaiword").click(function () {
        get_selection()
    })

    function seachWord(txt) {
        if (txt != '') {
            $.ajax({
                data: {
                    word: txt
                },
                type: 'POST',
                url: '/clickSearch',
                dataType: "json",
                success: (function (data) {
                    try {
                        var word = data.getData[0]
                        var wordClass = data.getData[1]
                        console.log(word)
                        console.log(wordClass)

                        // sendCommend(word)

                        var box = '<div class="clickTran_first">' + 'คำที่แปล ' + '<span class="clickTran_word">' + word + '</span></div>'
                        box += '<table>'
                        console.log("box:",box)

                        for (var i in wordClass) {
                            // console.log(i)
                            // console.log(wordClass[i])
                            // console.log(wordClass[i][num])
                            box += '<tr class="clickTran_trf">'
                                + '<td>' + '<span class="clickTran_class">' + i + '</span></td>'
                                + '</tr>'
                            for (var word in wordClass[i] ){
                                console.log(wordClass[i][word])
                                for (var s_word in wordClass[i][word]) {
                                    // word translated
                                    console.log(s_word)

                                    box += '<tr class="clickTranclickTran_trs">'
                                        +  '<td><span class="clickTran_wordtran">' + s_word + '</span></td>'
                                    for ( var s_wordSlated in wordClass[i][word][s_word]) {
                                        console.log(s_wordSlated)
                                        console.log(wordClass[i][word][s_word][s_wordSlated])

                                        if(s_wordSlated>0){
                                            box += '<span class="clickTran_comma">,</span> '
                                        }
                                        box += '<td><span class="clickTran_traned ">'+wordClass[i][word][s_word][s_wordSlated]+'</span>'
                                    }
                                }
                            }
                            box += '</tr>'
                        }
                        box += '</table>'


                        $('.translateword').empty()
                        $('.translateword').append(box)
                    } catch (err) {

                    }

                }),
                error: function (error) {
                    console.log(error)
                }
            });
        }
    }


    // function copy_textarea() {
    //     var copyText = document.getElementById("result_translate");
    //     copyText.select();
    //     copyText.setSelectionRange(0, 99999)
    //     document.execCommand("copy");
    //     alert("Copied the text: " + copyText.value);
    // }

// for translate in weppage
//     var first =true
// 	$('#translate').click(function () {
//         $.ajax({
// 			data : {
// 				sentence : $('#thaiword').val(),
// 			},
// 			type : 'POST',
// 			url : '/transtate',
//             success:(function(data) {
//                 $('#success').text(data.sentence).show();
//                 $('#error').hide()
//                 var sentence = data.sentence
//                 var tagesentence = document.createElement("P");
//                 for(i=0;i<sentence.length;i++){
//                      tagesentence.innerText = sentence[i];
//                      document.getElementById("showtran").appendChild(tagesentence);
//                      first = false;
//                 }
//             }),
//             error:function (error) {
//                 $('#success').hide()
//                 $('#error').text(error)
//             }
// 		});
//     })

    $('#translate2').click(function () {
        translate2()
    })
    var result = ""

    function translate2() {
        var value_textarea
        $('#clear_textarea').click(function () {
            value_textarea = $('textarea#thaiword').val("")
        })
        if ($('#clear_textarea') == onclick){
            sentence = value_textarea
        }else {
            sentence = $('#thaiword').val()
            // alert("else")
        }
        $.ajax({
            data: {
                sentence: sentence,
            },
            type: 'POST',
            url: '/transtate2',
            success: (function (data) {
                // console.log(typeof data)
                // console.log(data.length)
                // console.log(data)
                // console.log(data[0])
                // console.log(data[1])
                $("#result_translate").empty()
                // console.log(data)
                $('#input_hmongcommend').empty()
                var hmongcommend = ""
                var hmong = ""
                for (i = 0; i < data.length; i++) {
                    result = ""
                    hmongcommend = ""
                    for (j = 0; j < data[i].length; j++) {
                        // console.log(typeof data[i][0])
                        result += '<span class="span_result_translate" style="float: left">' + data[i][j] + "&nbsp; " + '</span>'
                        hmongcommend += data[i][j] + " "
                    }
                    hmong += hmongcommend + "\n"
                    $("#result_translate").append(result)
                    $("#result_translate").append("<br>")
                    $("#get_textarea").val(hmong)

                }

            }),
            error: function (error) {
                $('#success').hide()
                $('#error').text(error)
            }

        });

    }

    var x = 0
    $("#thaiword").keydown(function () {
        x++;
        if (x == 1) {
            setTime = setTimeout(function () {
                // console.log("1")
                tran()
                x = 0
            }, 100);
        } else {

            clearTimeout(setTime)
            wait_tran()

            setTime = setTimeout(function () {
                // console.log("1")
                tran()
                x = 0
            }, 200);

        }

        function wait_tran() {
            console.log("clear")
            var ww = result + '<span class="span_result_translate" style="float: left">' + "..." + '</span>'
            $("#result_translate").empty()
            $("#result_translate").append(ww)
        }

        function tran() {
            var word = $("#thaiword").val();

            $("#show").html(word);
            translate2();
        }
    });


    $('#pencil_button').click(function () {
        thaiCommend()
        hmong_commend()
    })
    function thaiCommend() {
        // $('#input_textCommend').empty()
        var thai = $('#thaiword').val()
        // console.log("thai:",thai)
        var thai_split = " "
        var t = " "
        t = thai.split("\n");  //ถ้าเจอวรรคแตกเก็บลง array t
        // console.log("plit_1:",t)

        $('#table_editcommend').empty()
        for(var i=0; i<t.length ; i++){
            // thai_split += t[i]+"<br/>"
            j = i + 1
            if (t[i] == ""){

            }else{
                thai_split = t[i]
                $('#table_editcommend').append("" +
                    "<tr class='tr_editcommend_"+j+"' id='tr_editcommend_"+j+"'>"+
                        "<th id='th_editcommend_"+j+"'>"+j+". ประโยคภาษาไทย : </th>"+
                        "<td id='td_editcommend_"+j+"'>" +
                            "<div id='input_textCommend_"+j+"' style='width: 250px; border: 0.7px solid rgba(42,50,48,0.39); border-radius: 5px; padding: 5px;'>" + thai_split + "</div>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_editcommend_"+j+"' id='tr_select_"+j+"'>"+
                        "<th id='th_select_"+j+"'>ผิดเรพาะ : </th>" +
                        "<td style='float: left' id='th2_'>" +
                            "<select class='form-control' name='select_commend_"+j+"' id='select_commend_"+j+"' style='width: 250px;'>" +
                                "<option value=''>เลือกชนิดที่ผิด</option>" +
                                "<option value='grammar'>ไวยากรณ์(grammar)</option>" +
                                "<option value='new'>มีคำใหม่(new)</option>" +
                            "</select>" +
                        "</td>"+
                    "</tr>" +
                    "<tr class='tr_editcommend_"+j+"'>" +
                        "<td>" +
                            "<hr size='1' width='100%'>"+
                        "</td>"+
                        "<td>" +
                            "<hr size='1' width='100%'>"+
                        "</td>"+
                    "</tr>"+
                 "")
            }
        }
    }
    // function sendCommend(word){
    //     var thai = $('#input_textCommend').val(word)
    //     console.log("thai :",thai)
    // }
    function hmong_commend(){
        var hmong = $("#get_textarea").val()
        var hmongword = hmong.split("\n");
        // console.log("hmongword :",hmongword)
        $('#table_editHmongcommend').empty()
        var j = 0
        for (var i=0; i<hmongword.length-1; i++){
            j++;
            if (hmongword[i] == ""){

            }else {
                $('#table_editHmongcommend').append("" +
                    "<tr class='tr_hmongcommend_"+j+"' id='tr_hmongcommend_"+j+"'>" +
                        "<th id='th_hmongcommend_"+j+"'>"+j+". คำแปลภาษาม้ง : </th>" +
                        "<td id='td_hmongcommend_"+j+"'>" +
                            "<div id='input_hmongcommend_"+j+"' style='width: 270px; border: 0.7px solid rgba(42,50,48,0.39); border-radius: 5px; padding: 5px;'>"+ hmongword[i] +"</div>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_hmongcommend_"+j+"' id='tr_editHmongcommend_"+j+"'>" +
                        "<th id='th_editHmongcommend_"+j+"'>แก้ไขความหมายของคุณ : </th>" +
                        "<td id='td_editHmongcommend_"+j+"'>" +
                            "<input type='text' class='form-control form-control' style='width: 270px; float: left' id='input_editHmongcommend_"+j+"'>" +
                        "</td>" +
                        "<td>" +
                            "<button type='button' value='"+j+"' class='color_button1' id='saveword_Hmongcommend' >บันทึก</button><span>  </span>" +
                            "<button type='button' value='"+j+"' class='color_button3' id='clearword_Hmongcommend'>ล้าง</button>" +
                        "</td>"+
                    "</tr>" +
                    "<tr class='tr_hmongcommend_"+j+"'>" +
                        "<td>" +
                            "<hr size='1' width='100%'>"+
                        "</td>"+
                        "<td>" +
                            "<hr size='1' width='100%'>"+
                        "</td>"+
                    "</tr>"+
                 "")
            }
        }
    }


    $('#clearword_eHmongcommend').click(function () {
        $('#textarea_editHmongcommend').empty()
        $('#textarea_editHmongcommend').val(" ")
    })

    $(this).on('click', 'button#saveword_Hmongcommend', function() {
        // $('button#saveword_Hmongcommend').click(function () {
        var num = $(this).val()
        var Hmongcommend = $('#input_editHmongcommend_' + num).val()
        var Thaicommend = $('#input_textCommend_' + num).text()
        var grammar = [];
        $.each($("#select_commend_" + num + " option:selected"), function () {
            grammar.push($(this).val());
        });
        grammar = grammar[0]
        // alert("You have selected the country - " + grammar.join(", "));
        console.log("Hmongcommend:", Hmongcommend)
        console.log("Thaicommend:", Thaicommend)
        console.log("grammar:", grammar)
        if (Hmongcommend != "") {
            if (confirm("ต้องการบันทึกหรือไม่")) {
                // alert("ต้องการบันทึก")
                insert_toRecommend()
            } else {
                alert("ไม่ต้องการบันทึก")
            }
        } else {
            alert("กรุณาป้อนข้อมูล")
        }

        function insert_toRecommend() {
            $.ajax({
                type: 'POST',
                url: '/getdata-user',
                success: (function (data) {
                    console.log("data garuser:",data)
                    var getUser = data.dataUser[1]
                    console.log("getUser_id:", getUser)
                    if (getUser != "") {
                        console.log("getUser:",getUser)
                        console.log("Thaicommend:",Thaicommend)
                        console.log("Hmongcommend:",Hmongcommend)
                        console.log("grammar:",grammar)
                        $.ajax({
                            type: 'POST',
                            url: '/insert_commendtoRecommend',
                            data: {
                                getUser_id: getUser,
                                Thaicommend: Thaicommend,
                                Hmongcommend: Hmongcommend,
                                grammar: grammar
                            },
                            success: (function (data) {
                                console.log("data state:",data.state)
                                if (data.state == true) {
                                    // alert("insert suscess")
                                    $(".tr_editcommend_" + num).remove();
                                    $(".tr_hmongcommend_" + num).remove();

                                    // document.getElementById("table_editHmongcommend").deleteRow(num);
                                    // document.getElementById("table_editcommend").deleteRow(num);
                                    // $("tr.tr_hmongcommend_" + num).empty()
                                    // $("tr.tr_editcommend_" + num).empty()
                                    alert("บันทึกสำเร็จ")
                                } else {
                                    alert("บันทึกไม่สำเร็จ!", data)
                                }
                            }),
                            error: function (error) {
                                console.log(error)
                            }
                        });
                    } else {
                        console.log("in else")
                        alert("ลงทะเบียนก่อน แนะนำแก้ไข")
                    }
                }),
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })


     $(this).on('click', 'button#clearword_Hmongcommend', function() {
         var num = $(this).val()
         $('#input_editHmongcommend_' + num).val("")
     })

    // function deleteRow(id){
    //     $("#" + id).remove();
    // }



    // from a NodeList
    autosize(document.querySelectorAll('textarea'));

    // from a single Node
    autosize(document.querySelector('textarea'));

    // from a jQuery collection
    autosize($('textarea'));

    $("textarea").resize(function () {

    });


    //copy text
    // $('#copy_button').click(function () {
    //     // var elm = $('div#result_translate').text()
    //     // console.log("elm:",elm)
    //     // $('#get_copy_textarea').append(elm)
    //     // var result = $('#get_copy_textarea').val()
    //     // console.log("result:",result)
    //     CopyToClipboard()
    // })
    //
    // function CopyToClipboard() {
    //     // var elm = document.getElementById("result_translate");
    //     // console.log("elm:",elm)
    //     var elm = $("#get_textarea").val()
    //     console.log("elm:",elm)
    //     // $('#get_copy_textarea').append(elm)
    //     // var result = $('#get_copy_textarea').val()
    //     // for Internet Explorer
    //
    //     if(document.body.createTextRange) {
    //         var range = document.body.createTextRange();
    //         range.moveToElementText(elm);
    //         range.select();
    //         document.execCommand("Copy");
    //         alert("Copied div content to clipboard");
    //     }
    //     else if(window.getSelection) {
    //         // other browsers
    //
    //         var selection = window.getSelection();
    //         var range = document.createRange();
    //         range.selectNodeContents(elm);
    //         selection.removeAllRanges(range);
    //         selection.addRange(range);
    //         document.execCommand("Copy");
    //         // alert("Copied div content to clipboard");
    //     }
    // }



    // ====== หน้าต่าง sidebar ===================================================================
    // function menubar() {
    //     document.getElementById("mySidenav").style.width = "250px";
    // }
    // function closeNav() {
    //     document.getElementById("mySidenav").style.width = "0";
    // }

})
