$(document).ready(function () {
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
        if (txt!=''){
            $.ajax({
			data : {
			    word : txt
            },
			type : 'POST',
			url : '/clickSearch',
            dataType: "json",
            success:(function(data) {
                try {
                    console.log(data.getData)
                    var word = data.getData
                    document.getElementById("wordselect").innerHTML = word
                }
                catch(err) {

                }
            }),
            error:function (error) {
                console.log(error)
            }
		});
        }
    }


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

    function translate2() {
        $.ajax({
            data: {
                sentence: $('#thaiword').val(),
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
                for (i = 0; i < data.length; i++) {
                    var result = ""
                    console.log( data)
                    for (j = 0; j < data[i].length; j++) {
                        console.log(typeof data[i])

                        if (data[i][j] > 1) {
                            result += '<span class="span_result_translate" style="float: left">' + data[i][0] + " &nbsp;" + '</span>'
                            console.log("11")
                        } else {
                            console.log("22")
                            result += '<span class="span_result_translate" style="float: left">' + data[i][j] + "&nbsp; " + '</span>'
                        }
                    }
                    $("#result_translate").append(result)
                    $("#result_translate").append("<br>")
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
                console.log("1")
                tran()
                x=0
            }, 200);
        }else {
            console.log("clear")
            clearTimeout(setTime)
            setTime = setTimeout(function () {
                console.log("1")
                tran()
                x=0
            }, 200);

        }

        function tran() {
            var word = $("#thaiword").val();
            $("#show").html(word);
            translate2();
        }
    });


    // from a NodeList
    autosize(document.querySelectorAll('textarea'));

    // from a single Node
    autosize(document.querySelector('textarea'));

    // from a jQuery collection
    autosize($('textarea'));

    $("textarea").resize(function () {

    });

})
