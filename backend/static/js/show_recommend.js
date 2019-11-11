$(document).ready(function () {

    show_addnewWord_newword()
    $(".show_checkWord_newword").hide()
    $(".show_addnewWord_newword").show()

    // wellcome-to-recommend
    $("#addnewWord_newword").click(function(){
        $(".show_checkWord_newword").hide()
        $(".show_addnewWord_newword").show()
        //alert("add");
        show_addnewWord_newword()
    });
    function show_addnewWord_newword(){
        $.ajax({
                type : 'POST',
                url : '/getdata-user',
                success:(function(data) {
                    var getsession = data.dataUser[1]
                    $.ajax({
                        data :{
                            userID : getsession
                        },

                        type : 'POST',
                        url : '/addnewWord-newword',
                        success:(function(data) {
                            // console.log(data)
                            $("#tbody_addnewWord_newword").empty()

                            for(i=0;i<data.length;i++){
                                var tr = "<tr align='center' id=tr_addnewWord_newword_"+data[i][0]+">"
                                tr += "<td>"+(i+1)+"</td>"
                                tr += "<td id=thaiword_addnewWord_newword_"+data[i][0]+">" + data[i][2] +"</td>"
                                tr += "<td id=select_addnewWord_newword_"+data[i][0]+"'>"  +
                                    " <select class=\"form-control\" id=\"selectclassword_addnewWord_newword_"+data[i][0]+"\">\n" +
                                    "   <option value=\"NOUN\">คำนาม(NOUN)</option>\n" +
                                    "   <option value=\"VERB\">คำกริยา(VERB)</option>\n" +
                                    "   <option value=\"ADP\">คำบุพบท(ADP)</option>\n" +
                                    "   <option value=\"AUX\">กริยาช่วย(AUX)</option>\n" +
                                    "   <option value=\"CCONJ\">คำเชื่อม(CCONJ)</option>\n" +
                                    "   <option value=\"DET\">คำบ่งชี้เฉพาะหรือไม่ชี้เฉพาะ(DET)</option>\n" +
                                    "   <option value=\"PRON\">คำสรรพนาม(PRON)</option>\n" +
                                    "   <option value=\"SCONJ\">คำสันธาน(SCONJ)</option>\n" +
                                    "   <option value=\"NUM\">ตัวเลข(NUM)</option>\n" +
                                    "   <option value=\"PART\">คำอนุภาคทั่วไป(PART)</option>\n" +
                                    "   <option value=\"ADJ\">คำคุณศัพท์(ADJ)</option>\n" +
                                    "   <option value=\"INTJ\">คำอุทาน(INTJ)</option>\n" +
                                    "   <option value=\"ADV\">คำวิเศษณ์(ADV)</option>\n" +
                                    "   <option value=\"PROPN\">คำนามชี้เฉพาะหรือวิสามานยนาม(PROPN)</option>\n" +
                                    "   <option value=\"X\">อื่นๆ(X)</option>\n" +
                                    "   </select>\n" +
                                    "   </td>"

                                tr += "<td>"+"<input class=\"form-control\" id=hmongword_addnewWord_newword_"+data[i][0]+" >"+"</td>"
                                tr += "<td>"+"<button class=\"btn btn-success btn-xs\" id=\"submit_addnewWord_newword\" value='"+data[i][0]+"' >ส่ง</button>"+"</td>"

                                tr += "</tr>"
                                $("#tbody_addnewWord_newword").append(tr)
                                $('#selectclassword_addnewWord_newword_'+data[i][0]).val((data[i][3]))

                            }
                        }),
                        error:function (error) {
                        }
                    });
                }),
                error:function (error) {
                    console.log(error)
                }
        });

    }

    $(this).on('click', 'button#submit_addnewWord_newword', function(){
        var id = $(this).val()
        var select = $('#selectclassword_addnewWord_newword_'+id).val()
        var wordthai = $('#thaiword_addnewWord_newword_'+id).text()
        var wordhmong = $('#hmongword_addnewWord_newword_'+id).val()
        // console.log(id)
        // console.log(select + wordhmong+ wordthai)
        $.ajax({
                type : 'POST',
                url : '/getdata-user',
                success:(function(data) {
                    // for get user login now
                    var getsession = data.dataUser[1]
                    alert(getsession+" "+id+" "+wordthai+" "+select+" "+wordhmong)

                    $("#tr_addnewWord_newword_"+id).hide(1500)

                }),
                error:function (error) {
                    console.log(error)
                }
            });
    })


    $("#checkWord_newword").click(function(){
        $(".show_checkWord_newword").show()
        $(".show_addnewWord_newword").hide()
        show_checkWord_newword()
      });

    function show_checkWord_newword() {
        $.ajax({
            type : 'POST',
            url : '/getdata-user',
            success:(function(data) {
                // for get user login now
                var getsession = data.dataUser[1]
                $.ajax({
                    data:{
                        userID: getsession
                    },
                    type : 'POST',
                    url : '/checkWord-Recommend',
                    success:(function(data) {
                        //console.log(data)
                        $("#tbody_checkWord_newword").empty()
                        for (i=0;i<data.length;i++){
                            // console.log(data[i][2]+" "+data[i][3])
                            var tr = "<tr id=tr_checkWord_Recommend_"+data[i][0]+">"
                            tr += "<td>"+(i+1)+"</td>"
                            tr += "<td id=thaiword_checkWord_newword_"+data[i][0]+">"+data[i][1]+"</td>"
                            tr += "<td id=hmong_checkWord_newword_"+data[i][0]+">"+data[i][2]+"</td>"

                            tr += "<td>"+"<button  class=\"btn btn-success btn-xs\" " +
                                "id=\"button_checkWord_newword\" for='true' value='"+data[i][0]+"'>ถูก</button>"+"</td>"

                            tr += "<td>"+"<button class=\"btn btn-danger btn-xs\" " +
                                "id=\"button_checkWord_newword\" for ='false' value='"+data[i][0]+"'>ผิด</button>"+"</td>"
                            $("#tbody_checkWord_newword").append(tr)
                        }
                    }),
                    error:function (error) {

                    }
                });
            }),
            error:function (error) {
                console.log(error)
            }
        })
    }

    $(this).on('click', 'button#button_checkWord_newword', function(){
        var id = $(this).val()
        var thaiword = $('#thaiword_checkWord_newword_'+id).val()
        var hmongword = $('#hmong_checkWord_newword_'+id).text()
        var check = $(this).attr("for")
        // console.log(id)
        // console.log(select + wordhmong+ wordthai)
        $.ajax({
                type : 'POST',
                url : '/getdata-user',
                success:(function(data) {
                    // for get user login now
                    var getsession = data.dataUser[1]
                    // console.log(getsession)
                    alert(getsession+" "+id+" "+thaiword+" "+hmongword+" "+check)
                    $("#tr_checkWord_Recommend_"+id).hide(1500)
                }),
                error:function (error) {
                    console.log(error)
                }
            });
    })


})