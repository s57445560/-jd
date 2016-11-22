/**
 * Created by 杨 on 2016/11/21.
 */
(function(jq) {
    jq.extend({
        'sunyang':function (form) {
            $(form).find('#tijiao').click(function () {
                var flag = true;
                $(form).find(':text,:password').each(function(){
                    $('#help_info').text('');
                    $(form).find(':text,:password').css('border-color','');
                    if($(this).val().length===0){
                        flag = false;
                        if($(this).prop('name')==='username'){
                            $('#help_info').text('账号不能为空');
                            $(this).css('border-color','red')
                        }else if($(this).prop('name')==='pwd'){
                            $('#help_info').text('密码不能为空');
                            $(this).css('border-color','red')
                        }
                        return false;
                    }
                    var minlen = parseInt($(this).attr('min-len'));
                    if($(this).val().length<minlen){
                        $('#help_info').text("账号长度不能小于"+minlen);
                        $(this).css('border-color','red');
                        flag = false;
                        return false;
                    }
                });
                if(flag){
                    $.ajax({
                        url:'/home/login/',
                        type:'POST',
                        dataType:'json',
                        data:{'user_name':$('#user_name').val(),'user_pwd':$('#user_pwd').val()},
                        success:function(data){
                            if(data.status){
                                location.href = '/home/'
                            }else {
                                $('#help_info').text(data.message);
                            }
                        },
                    })
                }
                return flag;
            });
        }
    });
})($);