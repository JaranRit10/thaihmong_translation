$(document).ready(function () {

    $('#clear_textarea').click(function () {
        $('textarea#thaiword').val("")
        translate2()
    })


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
                        console.log("data select:", data)
                        console.log("word:", word)
                        console.log("wordClass:", wordClass)

                        // sendCommend(word)

                        var box = '<div class="clickTran_first">' + 'คำที่แปล ' + '<span class="clickTran_word">' + word + '</span></div>'


                        box += '<table>'

                        for (var i in wordClass) {
                            // console.log(i)
                            // console.log(wordClass[i])
                            // console.log(wordClass[i][num])
                            box += '<tr class="clickTran_trf">'
                                + '<td>' + '<span class="clickTran_class">' + i + '</span></td>'
                                + '</tr>'
                            for (var word in wordClass[i]) {
                                console.log(wordClass[i][word])
                                for (var s_word in wordClass[i][word]) {
                                    // word translated
                                    console.log(s_word)

                                    box += '<tr class="clickTranclickTran_trs">'
                                        + '<td><span class="clickTran_wordtran">' + s_word + '</span></td>'
                                    for (var s_wordSlated in wordClass[i][word][s_word]) {
                                        console.log(s_wordSlated)
                                        console.log(wordClass[i][word][s_word][s_wordSlated])

                                        if (s_wordSlated > 0) {
                                            box += '<span class="clickTran_comma">,</span> '
                                        }
                                        box += '<td><span class="clickTran_traned ">' + wordClass[i][word][s_word][s_wordSlated] + '</span>'
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


    $('#translate2').click(function () {
        translate2()
    })
    var result = ""
    var DATARESPONSe
    var text = ""
    function translate2() {
        var value_textarea
        $('#clear_textarea').click(function () {
            value_textarea = $('textarea#thaiword').val("")
        })
        if ($('#clear_textarea') == onclick) {
            sentence = value_textarea
        } else {
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
                $('#input_hmongcommend').empty()
                for (i = 0; i < data.length; i++) {
                    DATARESPONSe = data
                    console.log("data", data)
                    result = ""
                    text = ""
                    var list, show
                    for (j = 0; j < data[i].length; j++) {

                        // console.log(typeof (data[i][j]))
                        if (typeof (data[i][j]) == "object") {
                            result += '<span class="span_result_translate" name="' + "" + (i + "-" + j) + '" id="' + "" + (i + "-" + j) + '" style="float: left">' + data[i][j][0] + "&nbsp;" + '<span class="subResultSentence" id="subResult_' + "" + (i + "-" + j) + '"></span>' + '</span>'

                        } else {
                            result += '<span class="span_result_translate" name="' + "" + (i + "-" + j) + '" style="float: left">' + data[i][j] + "&nbsp;" + '</span>'
                        }
                    }
                    text += result + "."
                    $("#result_translate").append(text)
                    $("#result_translate").append("<br>")
                }
            }),
            error: function (error) {
                $('#success').hide()
                $('#error').text(error)
            }
        });
    }

    $(this).on("click", ".span_result_translate", function (e) {
        var names = $(this).attr("name")
        var name = names.split('-')
        var data = DATARESPONSe[name[0]][name[1]]
        // alert(typeof (data))
        if (typeof (data) == 'object') {
            if ($('#subResult_' + names).is(':empty')) {
                // console.log("if 1")
                var box = '<div class="box_results">'
                // alert(data.length)
                for (var i = 0; i < data.length; i++) {
                    box += '<div class="row rowWord" name="' + "" + names + '">' + data[i] + '&nbsp;'+'</div>'
                }
                box += '</div>'
                $('#subResult_' + names).append(box)

                // $("#get_result_text").append(box)
            } else {
                // console.log("if 2")
                $('#subResult_' + names).empty()
            }
        }
        var css = {
            "position": "absolute",
            "width": "100%",
            "left": "15px",
            "top": "25px",
            "z-index": "1"

        }
        $('#subResult_' + names).css(css);
    });

    $(this).on("click", ".rowWord", function (e) {
        var names = $(this).attr("name")
        // alert(names)
        $('#' + names).text($(this).text())
    });


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

    var centend_select = 'แก้ไขความหมายของคุณ:'

    function thaiCommend() {
        var thai = $('#thaiword').val()
        var thai_split = " "
        var t = " "
        t = thai.split("\n");  //ถ้าเจอวรรคแตกเก็บลง array t
        $('#table_editcommend').empty()
        for (var i = 0; i < t.length; i++) {
            j = i + 1
            if (t[i] == "") {

            } else {
                thai_split = t[i]
                $('#table_editcommend').append("" +
                    "<tr class='tr_editcommend_" + j + "' id='tr_editcommend_" + j + "'>" +
                        "<th id='th_editcommend_" + j + "'>" + j + ". ประโยคภาษาไทย : </th>" +
                        "<td id='td_editcommend_" + j + "'>" +
                            "<div id='input_textCommend_" + j + "' style='width: 250px; border: 0.7px solid rgba(42,50,48,0.39); border-radius: 5px; padding: 5px;'>" + thai_split + "</div>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_editcommend_" + j + "' id='tr_select_" + j + "'>" +
                        "<th id='th_select_" + j + "'>ผิดเพราะ : </th>" +
                        "<td style='float: left' id='th2_'>" +
                            "<select class='form-control selectOption' name='" + j + "' id='select_commend_" + j + "' style='width: 250px;'>" +
                                "<option value=''>เลือกชนิดที่ผิด</option>" +
                                "<option value='grammar'>ไวยากรณ์(grammar)</option>" +
                                "<option value='new'>มีคำใหม่(new)</option>" +
                            "</select>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_editcommend_" + j + "'>" +
                        "<td>" +
                            "<hr size='1' width='100%'>" +
                        "</td>" +
                        "<td>" +
                            "<hr size='1' width='100%'>" +
                        "</td>" +
                    "</tr>" +
                    "")
            }
        }
    }

    function hmong_commend() {
        var hmong = $("#result_translate").text()
        var hmongword = hmong.split(".");
        // console.log("hmongword :",hmongword)
        $('#table_editHmongcommend').empty()
        var j = 0
        for (var i = 0; i < hmongword.length - 1; i++) {
            j++;
            if (hmongword[i] == "") {

            } else {
                $('#table_editHmongcommend').append("" +
                    "<tr class='tr_hmongcommend_" + j + "' id='tr_hmongcommend_" + j + "'>" +
                        "<th id='th_hmongcommend_" + j + "'>คำแปลภาษาม้ง : </th>" +
                        "<td id='td_hmongcommend_" + j + "'>" +
                            "<div id='input_hmongcommend_" + j + "' style='width: 270px; border: 0.7px solid rgba(42,50,48,0.39); border-radius: 5px; padding: 5px;'>" + hmongword[i] + "</div>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_hmongcommend_" + j + "' id='tr_editHmongcommend_" + j + "'>" +
                        "<th id='th_editHmongcommend_" + j + "'>" + centend_select + "</th>" +
                        "<td id='td_editHmongcommend_" + j + "'>" +
                            "<input type='text' class='form-control form-control' style=' float: left' id='input_editHmongcommend_" + j + "'>" +
                        "</td>" +
                        "<td>" +
                            "<button type='button' value='" + j + "' class='color_button1' id='saveword_Hmongcommend' >บันทึก</button><span>  </span>" +
                            "<button type='button' value='" + j + "' class='color_button3' id='clearword_Hmongcommend'>ล้าง</button>" +
                        "</td>" +
                    "</tr>" +
                    "<tr class='tr_hmongcommend_" + j + "'>" +
                        "<td>" +
                            "<hr size='1' width='100%'>" +
                        "</td>" +
                        "<td>" +
                            "<hr size='1' width='100%'>" +
                        "</td>" +
                    "</tr>" +
                    "")
            }
        }
    }

    $('#clearword_eHmongcommend').click(function () {
        $('#textarea_editHmongcommend').empty()
        $('#textarea_editHmongcommend').val(" ")
    })


    $(this).on('change', 'select.selectOption', function () {
        var elementName = $(this).attr('name')
        var num = $(this).val()
        // alert(num)
        // alert(elementName)
        if (num == '') {
            centend_select = 'แก้ไขความหมายของคุณ:'
            $('#th_editHmongcommend_' + elementName).empty('')
            $('#th_editHmongcommend_' + elementName).append(centend_select)
        }
        if (num == 'grammar') {
            centend_select = 'แก้ไขไวยากรณ์:'
            $('#th_editHmongcommend_' + elementName).empty('')
            $('#th_editHmongcommend_' + elementName).append(centend_select)
            // alert(centend_select)
        }
        if (num == 'new') {
            centend_select = 'แก้ไขคำใหม่:'
            $('#th_editHmongcommend_' + elementName).empty('')
            $('#th_editHmongcommend_' + elementName).append(centend_select)
        }
    })


    $(this).on('click', 'button#saveword_Hmongcommend', function () {
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
                    console.log("data garuser:", data)
                    var getUser = data.dataUser[1]
                    console.log("getUser_id:", getUser)
                    if (getUser != "") {
                        console.log("getUser:", getUser)
                        console.log("Thaicommend:", Thaicommend)
                        console.log("Hmongcommend:", Hmongcommend)
                        console.log("grammar:", grammar)
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
                                console.log("data state:", data.state)
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

    $(this).on('click', 'button#clearword_Hmongcommend', function () {
        var num = $(this).val()
        $('#input_editHmongcommend_' + num).val("")
    })

    // from a NodeList
    autosize(document.querySelectorAll('textarea'));

    // from a single Node
    autosize(document.querySelector('textarea'));

    // from a jQuery collection
    autosize($('textarea'));

    $("textarea").resize(function () {

    });
    var xx = 1;
    $(".input-user-signUp").keyup(function () {
        var user = $(this).val()
        console.log(user)
        checkUser_signup(user)

    })

    $("span#checkusersignUpF").hide()
    $("span#checkusersignUpT").hide()

    function checkUser_signup(username) {
        $.ajax({
            data: {
                name_signUp: username
            },
            type: 'POST',
            url: '/checksignup',
            success: (function (check) {
                console.log(check)
                if (check == 1) {
                    $("span#checkusersignUpF").hide()
                    $("span#checkusersignUpT").show()
                } else {
                    $("span#checkusersignUpT").hide()
                    $("span#checkusersignUpF").show()
                }

            }),
            error: function (error) {
                console.log(error)
            }
        });

    }

    $("#form-signUp").submit(function (event) {
        function strip(str) {
            return str.replace(/^\s+|\s+$/g, '');
        }

        var fname = strip($("#fname_signup").val())
        var lname = strip($('#lname_signup').val())
        var email = $("#email_signup").val()
        var username = strip($('#username_signup').val())
        var pass = strip($("#password_signup").val())
        var cpass = strip($("#cpassword_signup").val())

        if (fname != "" && lname != "" && email != "" && username != "" && (cpass == pass) &&
            (pass.length > 5)) {
            createnewUser(fname, lname, email, username, pass)
            // alert("OK")
            // alert(fname + lname + email + username + pass)

        } else {
            alert("ไม่สามารถสมัครได้โปรดลองอีกครั้ง")
        }
    });

    function createnewUser(fname, lname, email, username, pass) {
        $.ajax({
            type: 'POST',
            url: '/signup',
            data: {
                fname: fname,
                lname: lname,
                email: email,
                username: username,
                pass: pass,

            },
            success: (function (ckeck) {
                if (ckeck == 1) {
                    alert("สมัครสมาชิกเรียบร้อย")

                } else {
                    alert("ไม่สามารถทำการสมัครสมาชิกได้")
                }
            }),
            error: function (error) {
                console.log(error)
            }
        });
    }

    function resizeTageselect() {
        $("#widthTempOption").html($('#resizingSelectTag option:selected').text());
        $('#resizingSelectTag').width($("#selectTagWidth").width());
    }

    resizeTageselect()
    // resize tage select on index page
    $('#resizingSelectTag').change(function () {
        resizeTageselect()
    });


    //copy text
    $('#copy_button').click(function () {
        CopyToClipboard()
    })

    function CopyToClipboard() {
        if (document.body.createTextRange) {
            var range = document.body.createTextRange();
            range.moveToElementText(result_translate);
            range.select();
            document.execCommand("Copy");
            alert("Copied div content to clipboard");
        } else if (window.getSelection) {
            // other browsers

            var selection = window.getSelection();
            var range = document.createRange();
            range.selectNodeContents(result_translate);
            selection.removeAllRanges(range);
            selection.addRange(range);
            document.execCommand("Copy");
            // alert("Copied div content to clipboard");
        }
    }


});