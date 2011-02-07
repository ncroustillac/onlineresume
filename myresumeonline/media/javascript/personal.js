    function getContent(selection) {
        $.get('./'+selection, function(datas) {
            $('#content-wrap').html(datas);
            $('.content .contentDatas').hide();
            $('.content .contentDatas#desc').show('slow');
            $('.content input').click(function() { 
                var content = $(this).parents('.content').attr('id');
                $('#'+content+' .contentDatas').hide();
                $('#'+content+' .contentDatas#'+this.id).show('slow');
                });
            });
    }

