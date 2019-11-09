$(document).ready( function () {

    $('.data_reccommend').show()
    $('.data_newword').hide()


    $('#getRecommend').click(function () {
        getRecommend()
        $("tbody#tbody_getnewword").empty()
        $('.data_reccommend').show()
        $('.data_newword').hide()
    });

    $('#getNewword').click(function () {
        getNewword()
        $('.data_reccommend').hide()
        $('.data_newword').show()
    });

    // getNewword()
    // getRecommend()
    function getRecommend() {
        $.ajax({
            type : 'POST',
            url : '/getRecommend',
            success:(function(data) {
                // console.log(data.getData.length)
                $("tbody#tbody_getrecommend").empty()
                var count=1;
                for (x of data.getData) {

                    $("tbody#tbody_getrecommend").append(
                        "<tr align='center' id='trRecommend_"+ x[0] +"'>" +
                            "<td class='recommendRow' name='"+x[0]+"' id='tdRecommend_id_"+ x[0] +"'>" + count + "</td>" +
                            "<td class='recommendRow' id='tdRecommend_thaiword_"+ x[0] +"'>" + x[2] + "</td>" +
                            "<td class='recommendRow' id='tdRecommend_hmongword_"+ x[0] +"'>" + x[3] + "</td>" +
                            "<td class='recommendRow' id='tdRecommend_time_"+ x[0] +"'>" + x[1] + "</td>" +
                            "<td class='recommendRow' id='tdRecommend_type_"+ x[0] +"'>" + x[4] + "</td>" +

                            "<td class='contro_recommendRow' id='edit_recommendRow_"+ x[0] +"'>" +
                            "<button type='button' class='btn color_button2 btn-xs' " +
                            "data-toggle='modal' data-target='#add_recommend' id='edit_tdRecommend' " +
                            " style='margin-right: ;' value='"+x[0]+"'><i class=\"pencil alternate icon\"></i>Edit</button></td>" +

                            "<td class='contro_recommendRow' id='delete_recommendRow_"+ x[0] +"'>" +
                            "<button type='button' class='btn color_button2 btn-xs' data-toggle='modal' data-target='#deleteRow_recommend' " +
                            "id='delete_tdRecommend' value='"+x[0]+"'><i class=\"eraser icon\"></i>Delete</button></td>" +
                        "</tr>"
                    );
                    "<br>"
                    count= count+1;
                }
                paginationRecommend(data.getData.length)
                // deleteRow()
            }),
            error:function(error) {
                console.log(error)
            }
        });
    }

    // show model rows recommend
    $(this).on('click', 'button#edit_tdRecommend', function(){
        var idsentence = $(this).val()
        var numbersentence = $("#tdRecommend_id_"+idsentence).text();
        var thaisentence = $("#tdRecommend_thaiword_"+idsentence).text();
        var hmongsentence = $('#tdRecommend_hmongword_'+idsentence).text();
        var grammarsentence = $('#tdRecommend_type_'+idsentence).text();

        console.log(idsentence+" "+thaisentence+" "+hmongsentence+""+grammarsentence)
        $('td#thaisentence').empty()
        $('td#hmongsentence').empty()
        $('td#grammarsentence').empty()
        $('td#thaisentence').append(thaisentence)
        $('td#hmongsentence').append(hmongsentence)
        $('td#grammarsentence').append(grammarsentence)
        $('input#input_thaisentence').val(thaisentence)
        $('input#input_hmongsentence').val(hmongsentence)
        $('input#input_grammarsentence').val(grammarsentence)

        var saveThai_recommend
        var saveHmong_recommend
        var saveGrammar_recommend
        $('button#saveword_editRecommend').click(function () {
            saveThai_recommend = $('input#input_thaisentence').val()
            saveHmong_recommend = $('input#input_hmongsentence').val()
            saveGrammar_recommend = $('input#input_grammarsentence').val()
            console.log("thai:",saveThai_recommend)
            console.log("hmong:",saveHmong_recommend)
            console.log("grammar:",saveGrammar_recommend)
            console.log("id:",idsentence)

            saveRecommend()
            function saveRecommend() {
                $.ajax({
                    data : {
                        id_recommend:idsentence,
                        Thai_recommend:saveThai_recommend,
                        Hmong_recommend:saveHmong_recommend,
                        Grammar_recommend:saveGrammar_recommend
                    },
                    type : 'POST',
                    url : '/save_wordRecommend',
                    success:(function(data) {
                        // alert("data:",data)
                        if (data.state == true){
                            getRecommend()
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

        $('button#clearword_editRecommend').click(function () {
            $('input#input_thaisentence').val(" ")
            $('input#input_hmongsentence').val(" ")
            $('input#input_grammarsentence').val(" ")
        })

    })

    $(this).on('click', 'button#delete_tdRecommend',function (){
        var iddelete = $(this).val()
        console.log("id:",iddelete)
        var numbersentence = $("#tdRecommend_id_"+iddelete).text();
        var thaisentence = $("#tdRecommend_thaiword_"+iddelete).text();
        var hmongsentence = $('#tdRecommend_hmongword_'+iddelete).text();
        var grammarsentence = $('#tdRecommend_type_'+iddelete).text();
        console.log("numbersentence:",numbersentence)
        console.log("thaisentence:",thaisentence)
        console.log("hmongsentence:",hmongsentence)
        console.log("grammarsentence:",grammarsentence)
        deleterow()
        function deleterow() {
            $('button#delet_row').on('click',function () {
                var rowid = $('#trRecommend_'+iddelete)
                console.log("rowid:",rowid)
                // document.getElementById("tableRecommend").deleteRow(idrow);
                $.ajax({
                    data: {
                        id_recommend:iddelete,
                        Thai_recommend:thaisentence,
                        Hmong_recommend:hmongsentence,
                        Grammar_recommend:grammarsentence
                    },
                    type: 'POST',
                    url: '/delete_Recommend',
                    dataType: "json",
                    success: (function (data) {
                        if (data.state == true) {
                            getRecommend()
                            alert("ทำการลบสำเร็จ")
                            // seachWord_Admin()
                        } else {
                            alert("ทำการลบไม่สำเร็จ")
                        }
                    }),
                    error: function (error) {
                        console.log(error)
                    }
                });
            })

        }
    })



    // pagination
    var tableR = '#tableRecommend';
    function paginationRecommend(length_rowRecommend) {
        // reset num button page
        $('.pagination_Recommend').html('')

        var check_maxRows = ($("#select_maxrow_Recommend").val())
        // console.log("max-check :"+check_maxRows)
        if(check_maxRows=='all'){
            maxRows = length_rowRecommend
        }else {
            maxRows = check_maxRows
        }
        var totalRows = length_rowRecommend

        // console.log('maxRows ='+maxRows)
        // console.log('totalRows ='+totalRows)

        var trnum = 0;
        $(tableR+' tr:gt(0)').each(function () {
            trnum++
            if(trnum > maxRows){
                $(this).hide()
            }
            if(trnum <= maxRows){
                $(this).show()
            }
        });

        // create button to page
        if (totalRows > maxRows){
            var pagenum = Math.ceil(totalRows/maxRows);
            var lastPage = 0
            lastPage = pagenum
            for(var i=1;i<=pagenum;){
                $('.pagination_Recommend').append('<button class="pageButton" id="'+i+'">' +
                    '<span>'+ i++ +'<span class="sr-only">(current)</span></span></button>').show()
            }
        }
        // show rows pervios button
        $('#startRow_Recommend').text(1)
        $('#endRow_Recommend').text((maxRows))
        $('#totalRow_Recommend').text(totalRows)

        // click select button
        $('.pageButton:first-child').addClass('color_button3');
        $('.pageButton').on('click',function () {
            var pageNum = this.id
            // active button
            $('.pageButton').removeClass('color_button3');
            $(this).addClass('color_button3');

            var row
            var trIndex = 0;
            //loop show rows
            $(tableR+' tr:gt(0)').each(function () {
                trIndex++
                if(trIndex > (maxRows*pageNum) || trIndex <= (maxRows*pageNum)-maxRows){
                    $(this).hide()
                }else {
                    $(this).show()
                }
            })

            $('#startRow_Recommend').text(((maxRows*pageNum)-maxRows)+1)

            if (pageNum == lastPage){
                $('#endRow_Recommend').text((totalRows))
            } else {
                $('#endRow_Recommend').text((maxRows*pageNum))
            }
            $('#totalRow_Recommend').text(totalRows)
        })

    } // end funtion pagination
    // click class select
    $('#select_maxrow_Recommend').on('change',function() {
        getRecommend()
    })




    // funtion getNewword ===========================
    // getNewword()
    // var length_rowNewword
    function getNewword() {
        $.ajax({
            type: 'POST',
            url: '/getNewword',
            success: (function (data) {
                // length_rowNewword = data.getData.length
                // console.log('length_rowNewword '+length_rowNewword)
                // console.log(data.getData.length)
                $("tbody#tbody_getnewword").empty()
                var coute = 1;
                for (x of data.getData) {
                    $("tbody#tbody_getnewword").append(
                        "<tr align='center' id='trNewword' >" +
                            "<td class='trNewword' name='"+x[0]+"' id='trNewword_id_"+ x[0] +"'>" + coute + "</td>" +
                            "<td class='trNewword' id='trNewword_Sentence_id_"+ x[0] +"'>" + x[1] + "</td>" +
                            "<td class='trNewword' id='trNewword_thaiword_"+  x[0] +"'>" + x[2] + "</td>" +
                            "<td class='trNewword' id='trNewword_hmongword_"+    x[0] +"'>" + x[3] + "</td>" +
                            "<td class='trNewword' id='trNewword_New_word_"+    x[0] +"'>" + x[4] + "</td>" +

                            "<td class='contro_newwordRow'>" +
                            "<button type='button' class='btn color_button2 btn-xs' " +
                            "data-toggle='modal' data-target='#edit_newword' id='edit_tdNewword' " +
                            " style='margin-right: 2px;' value='"+x[0]+"'><i class=\"pencil alternate icon\"></i>Edit</button></td>" +

                            "<td class='contro_newwordRow'>" +
                            "<button type='button' class='btn color_button2 btn-xs' data-toggle='modal' data-target='#deleteRow_mewword' " +
                            "id='delete_newword' value='"+x[0]+"'><i class=\"eraser icon\"></i>Delete</button></td>" +
                        "</tr>"
                    );
                    coute = coute+1;
                }

                var date = data.getData[0][1]
                console.log('new_date'+date)

                var d = new Date(date);
                console.log('new_d'+d)

                paginationNewword(data.getData.length)
            }),
            error: function(error) {
                console.log(error)
            }
        });
    } //end funtion

    // show model rows recommend
    $(this).on('click', 'button#edit_tdNewword', function(){
        // checkSelect()
        var idWord = $(this).val()
        var thaiWord = $("#trNewword_thaiword_"+idWord).text();
        var hmongWord = $("#trNewword_hmongword_"+idWord).text();
        var typWord = $('#trNewword_New_word_'+idWord).text();

        console.log(idWord+" "+thaiWord+" "+hmongWord+" "+typWord)

        $('input#input_thaiWord').val(thaiWord)
        $('input#input_hmongWord').val(hmongWord)
        // $('select#select_newword').val(hmongWord)


        // click save newword
        $('button#saveNewword').click(function () {
            var thaiword = $('input#input_thaiWord').val()
            var hmongword = $('input#input_hmongWord').val()
            var typword = $('select#select_newword').val()
            console.log("thaiword:",thaiword)
            console.log("hmongword:",hmongword)
            console.log("typword:",typword)
            saveNewword()
            function saveNewword() {
                $.ajax({
                    data : {
                        id_newword:idWord,
                        Thai_newword:thaiword,
                        Hmong_newword:hmongword,
                        tpy_newword:typword
                    },
                    type : 'POST',
                    url : '/save_Newword',
                    success:(function(data) {
                        // alert("data:",data)
                        if (data.state == true){
                            getNewword()
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
        })//end button save newword
    }) //end button edit newword

    $(this).on('click', 'button#delete_newword', function(){
        var idWord = $(this).val()
        var thaiWord = $("#trNewword_thaiword_"+idWord).text();
        var hmongWord = $("#trNewword_hmongword_"+idWord).text();
        var typWord = $('#trNewword_New_word_'+idWord).text();

        console.log(idWord+" "+thaiWord+" "+hmongWord+" "+typWord)

        // click save newword
        $('button#save_model_newword').click(function () {
            // var thaiword = $('input#input_thaiWord').val()
            // var hmongword = $('input#input_hmongWord').val()
            // var typword = $('select#select_newword').val()
            // console.log("thaiword:",thaiword)
            // console.log("hmongword:",hmongword)
            // console.log("typword:",typword)
            deleteNewword()
            function deleteNewword() {
                $.ajax({
                    data : {
                        id_newword:idWord,
                        Thai_newword:thaiWord,
                        Hmong_newword:hmongWord,
                        tpy_newword:typWord
                    },
                    type : 'POST',
                    url : '/delete_Newword',
                    success:(function(data) {
                        // alert("data:",data)
                        if (data.state == true){
                            getNewword()
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
        })//end button save newword
    }) //end button edit newword

    // select newword
     $('select#select_newword').change(function () {
        checkSelect()
    })
    function checkSelect() {
        // var check_valueSelect = ($("#select_newword").val())
        // console.log("select:",check_valueSelect)
        // document.getElementById("select_value").value = check_valueSelect;

        var select = document.getElementById("select_newword");
        console.log("select:",select)
        var option = select.options[select.selectedIndex];
        console.log("option:",option)
        if (option.id == "NOUN")
        {
            document.getElementById("select_newword").value = option.text;
        }
        else if(option.id == "VERB"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "ADP"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "AUX"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "CCONJ"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "DET"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "PRON"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "SCONJ"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "NUM"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "PART"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "ADJ"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "INTJ"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "ADV"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "PROPN"){
            document.getElementById("select_value").value = option.text;
        }
        else if(option.id == "X"){
            document.getElementById("select_value").value = option.text;
        }
    }

    // pagination newword
    var tableN = '#tableNewword';
    function paginationNewword(length_rowNewword) {
        // reset num button page
        $('.pagination_Newword').html('')

        var check_maxRows_newword = ($("#select_maxrow_newword").val())
        // console.log("max-check :"+check_maxRows)
        if(check_maxRows_newword =='all'){
            maxRows_newword = length_rowNewword
        }else {
            maxRows_newword = check_maxRows_newword
        }
        var totalRows_newword = length_rowNewword

        // console.log('length_rowNewword ='+length_rowNewword)
        // console.log('totalRows ='+totalRows)

        var trnum_newword = 0;
        $(tableN+' tr:gt(0)').each(function () {
            trnum_newword++
            if(trnum_newword > maxRows_newword){
                $(this).hide()
            }
            if(trnum_newword <= maxRows_newword){
                $(this).show()
            }
        });

        // create button to page
        if (totalRows_newword > maxRows_newword){
            var pagenum_newword = Math.ceil(totalRows_newword/maxRows_newword);
            var lastPage_newword = 0
            lastPage_newword = pagenum_newword
            for(var i=1;i<=pagenum_newword;){
                $('.pagination_Newword').append('<button class="pageButton_newword color_button3" id="'+i+'">' +
                    '<span>'+ i++ +'<span class="sr-only">(current)</span></span></button>').show()
            }
        }
        // show rows pervios button
        $('#startRow_Newword').text(1)
        $('#endRow_Newword').text((maxRows_newword))
        $('#totalRow_Newword').text(totalRows_newword)

        // click select button
        $('.pageButton_Newword:first-child').addClass('color_button3');
        $('.pageButton_newword').on('click',function () {
            var pageNum_newword = this.id
            // active button
            $('.pageButton_newword').removeClass('color_button3');
            $(this).addClass('color_button3');

            // var row
            var trIndex_newword = 0;
            //loop show rows
            $(tableN+' tr:gt(0)').each(function () {
                trIndex_newword++
                if(trIndex_newword > (maxRows_newword*pageNum_newword) || trIndex_newword <= (maxRows_newword*pageNum_newword)-maxRows_newword){
                    $(this).hide()
                }else {
                    $(this).show()
                }
            })

            $('#startRow_Newword').text(((maxRows_newword*pageNum_newword)-maxRows_newword)+1)

            if (pageNum_newword == lastPage_newword){
                $('#endRow_Newword').text((totalRows_newword))
            } else {
                $('#endRow_Newword').text((maxRows_newword*pageNum_newword))
            }
            $('#totalRow_Newword').text(totalRows_newword)
        })

    } // end funtion pagination
    // click class select
    $('#select_maxrow_newword').on('change',function() {
        getNewword()
    })


    // SideNav Initialization
    
    // $(".button-collapse").sideNav();


}); //end ready

