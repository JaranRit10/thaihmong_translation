$(document).ready( function () {

        $('.data_reccommend').show()
        $('.data_newword').hide()


        $('#getRecommend').click(function () {
            $('.data_reccommend').show()
            $('.data_newword').hide()
        });

        $('#getNewword').click(function () {
            // getNewword()
            $('.data_reccommend').hide()
            $('.data_newword').show()
        });

        getRecommend()
        function getRecommend() {
            $.ajax({
                type : 'POST',
                url : '/getRecommend',
                success:(function(data) {
                    // console.log(data.getData.length)
                   $("tbody#tbody_getrecommend").empty()
                    for (x of data.getData) {

                        $("tbody#tbody_getrecommend").append(
                            "<tr id='trRecommend' >" +
                                "<td class='recommendRow' id='tdRecommend_id_"+ x[0] +"'>" + x[0] + "</td>" +
                                "<td class='recommendRow' id='tdRecommend_thaiword_"+ x[0] +"'>" + x[2] + "</td>" +
                                "<td class='recommendRow' id='tdRecommend_hmongword_"+ x[0] +"'>" + x[3] + "</td>" +
                                "<td class='recommendRow' id='tdRecommend_time_"+ x[0] +"'>" + x[1] + "</td>" +
                                "<td class='recommendRow' id='tdRecommend_type_"+ x[0] +"'>" + x[4] + "</td>" +

                                "<td class='contro_recommendRow'>" +
                                    "<button type='button' class='btn btn-success btn-xs' " +
                                    "data-toggle='modal' data-target='#add_recommend' id='edit_tdRecommend' " +
                                    " style='margin-right: 2px;' value='"+x[0]+"'><i class=\"pencil alternate icon\"></i>Edit</button></td>" +
                                "<td class='contro_recommendRow'>" +
                                    "<button type='button' class='btn btn-success btn-xs' data-toggle='modal' data-target='#deleteRow_recommend' " +
                                    "id='delte_searchword' value='"+x[0]+"'><i class=\"eraser icon\"></i>Delete</button></td>" +
                            "</tr>"
                        );
                        "<br>"

                    }
                    paginationRecommend(data.getData.length)
                 }),
                error:function(error) {
                    console.log(error)
                }
            });
        }

        // show model rows recommend
        $(this).on('click', 'button#edit_tdRecommend', function(){
            var idsentence = $(this).val()
            var thaisentence = $("#tdRecommend_thaiword_"+idsentence).text();
            var hmongsentence = $('#tdRecommend_hmongword_'+idsentence).text();

            console.log(idsentence+" "+thaisentence+" "+hmongsentence)
             $('td#thaisentence').empty()
             $('td#hmongsentence').empty()
             $('td#thaisentence').append(thaisentence)
             $('td#hmongsentence').append(hmongsentence)
             $('input#input_thaisentence').val(thaisentence)
             $('input#input_hmongsentence').val(hmongsentence)

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
            $('.pageButton:first-child').addClass('paginationButton');
            $('.pageButton').on('click',function () {
                var pageNum = this.id
                // active button
                $('.pageButton').removeClass('paginationButton');
                $(this).addClass('paginationButton');

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

        // updateword_Recommend()
        function updateword_Recommend(){
            $('button#saveword_editRecommend').click(function () {
                editThai_recommend = $('input#input_thaisentence').val()
                editHmong_recommend = $('input#input_hmongsentence').val()

                if (editThai_recommend ){
                    alert('กรุณากรอกข้อมูลใหม่')
                } else {
                    console.log('editthai '+editThai_recommend)
                    console.log('editHmong '+editHmong_recommend)
                }
            })

            $('button#clearword_editRecommend').click(function () {
                $('input#input_thaisentence').empty()
                $('input#input_hmongsentence').empty()
            })
            // return editThai_recommend,editHmong_recommend
        }


        // funtion getNewword ===========================
        getNewword()
        // var length_rowNewword
        function getNewword() {
            $.ajax({
                type: 'POST',
                url: '/getNewword',
                success: (function (data) {
                    // length_rowNewword = data.getData.length
                    // console.log('length_rowNewword '+length_rowNewword)
                    // console.log(data.getData.length)
                    for (x of data.getData) {
                        $("tbody#tbody_getnewword").append(
                            "<tr id='trNewword' >" +
                                "<td class='trNewword' id='trNewword_id_"+          x[0] +"'>" + x[0] + "</td>" +
                                "<td class='trNewword' id='trNewword_Sentence_id_"+ x[0] +"'>" + x[1] + "</td>" +
                                "<td class='trNewword' id='trNewword_Use_update_"+  x[0] +"'>" + x[2] + "</td>" +
                                "<td class='trNewword' id='trNewword_New_word_"+    x[0] +"'>" + x[3] + "</td>" +
                                "<td class='trNewword' id='trNewword_Num_Recommennd_"+ x[0] +"'>" + x[4] + "</td>" +

                                "<td class='contro_newwordRow'>" +
                                    "<button type='button' class='btn btn-success btn-xs' " +
                                    "data-toggle='modal' data-target='#edit_newword' id='edit_tdNewword' " +
                                    " style='margin-right: 2px;' value='"+x[0]+"'><i class=\"pencil alternate icon\"></i>Edit</button></td>" +

                                "<td class='contro_newwordRow'>" +
                                    "<button type='button' class='btn btn-success btn-xs' data-toggle='modal' data-target='#deleteRow_mewword' " +
                                    "id='delete_newword' value='"+x[0]+"'><i class=\"eraser icon\"></i>Delete</button></td>" +
                            "</tr>"
                            );
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
            var idWord = $(this).val()
            var thaiWord = $("#trNewword_New_word_"+idWord).text();
            var hmongWord = $('#input_hmongWord'+idWord).text();

            console.log(idWord+" "+thaiWord+" "+hmongWord)
             // $('td#thaiWord').empty()
             // $('td#hmongWord').empty()
             // $('td#thaiWord').append(thaiWord)
             // $('td#hmongWord').append(hmongWord)
             $('input#input_thaiWord').val(thaiWord)
             // $('input#input_hmongWord').val(hmongWord)

        })

    // pagination newword
    //     var tableN = '#tableNewword';
    //     function paginationNewword(length_rowNewword) {
    //         // reset num button page
    //         $('.pagination_Newword').html('')
    //
    //         var check_maxRows_newword = ($("#select_maxrow_newword").val())
    //         // console.log("max-check :"+check_maxRows)
    //         if(check_maxRows_newword =='all'){
    //             maxRows_newword = length_rowNewword
    //         }else {
    //             maxRows_newword = check_maxRows_newword
    //         }
    //         var totalRows_newword = length_rowNewword
    //
    //         // console.log('length_rowNewword ='+length_rowNewword)
    //         // console.log('totalRows ='+totalRows)
    //
    //         var trnum_newword = 0;
    //         $(tableN+' tr:gt(0)').each(function () {
    //             trnum_newword++
    //             if(trnum_newword > maxRows_newword){
    //                 $(this).hide()
    //             }
    //             if(trnum_newword <= maxRows_newword){
    //                 $(this).show()
    //             }
    //         });
    //
    //         // create button to page
    //         if (totalRows_newword > maxRows_newword){
    //             var pagenum_newword = Math.ceil(totalRows_newword/maxRows_newword);
    //             var lastPage_newword = 0
    //             lastPage_newword = pagenum_newword
    //             for(var i=1;i<=pagenum_newword;){
    //                 $('.pagination_Newword').append('<button class="pageButton_newword" id="'+i+'">' +
    //                     '<span>'+ i++ +'<span class="sr-only">(current)</span></span></button>').show()
    //             }
    //         }
    //         // show rows pervios button
    //         $('#startRow_Newword').text(1)
    //         $('#endRow_Newword').text((maxRows_newword))
    //         $('#totalRow_Newword').text(totalRows_newword)
    //
    //         // click select button
    //         $('.pageButton_Newword:first-child').addClass('btn btn-danger');
    //         $('.pageButton_newword').on('click',function () {
    //             var pageNum_newword = this.id
    //             // active button
    //             $('.pageButton_newword').removeClass('btn btn-danger');
    //             $(this).addClass('btn btn-danger');
    //
    //             // var row
    //             var trIndex_newword = 0;
    //             //loop show rows
    //             $(tableN+' tr:gt(0)').each(function () {
    //                 trIndex_newword++
    //                 if(trIndex_newword > (maxRows_newword*pageNum_newword) || trIndex_newword <= (maxRows_newword*pageNum_newword)-maxRows_newword){
    //                     $(this).hide()
    //                 }else {
    //                     $(this).show()
    //                 }
    //             })
    //
    //             $('#startRow_Newword').text(((maxRows_newword*pageNum_newword)-maxRows_newword)+1)
    //
    //             if (pageNum_newword == lastPage_newword){
    //                 $('#endRow_Newword').text((totalRows_newword))
    //             } else {
    //                 $('#endRow_Newword').text((maxRows_newword*pageNum_newword))
    //             }
    //             $('#totalRow_Newword').text(totalRows_newword)
    //         })
    //
    //     } // end funtion pagination
        // click class select
        $('#select_maxrow_Recommend').on('change',function() {
                getNewword()
        })
        // SideNav Initialization

        // $(".button-collapse").sideNav();


}); //end ready

$(document).ready( function () {

});