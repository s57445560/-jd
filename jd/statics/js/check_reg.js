/**
 * Created by 杨 on 2016/11/21.
 */

(function(jq) {
    jq.extend({
        'sunyang':function (form) {
            $('#tijiao').click(function () {
                var flag = true;
                $(form).find(':text,:password').each(function(i){
                    $('span').text('');
                    $(form).find(':text,:password').css('border-color','');
                    if($(this).val().length===0){
                        flag = false;
                        console.log($(this).parent().next().find('span'));
                        if($(this).prop('id')==='user_name'){
                            $(this).parent().next().find('span').text('账号不能为空');
                            $(this).css('border-color','red')
                        }else if($(this).prop('id')==='user_pwd'){
                            $(this).parent().next().find('span').text('密码不能为空');
                            $(this).css('border-color','red')
                        }else if($(this).prop('id')==='user_pwd_r'){
                            $(this).parent().next().find('span').text('密码不能为空');
                            $(this).css('border-color','red')
                        }
                        return false;
                    }
                    var min_len = parseInt($(this).attr('min-len'));
                    if($(this).val().length<min_len){
                        $(this).parent().next().find('span').text("长度不能小于"+min_len);
                        flag = false;
                        return false;
                    }
                    
                    if($(this).prop('id')==='user_pwd_r'){
                        var pwd_1 = $('#user_pwd').val();
                        var pwd_2 = $('#user_pwd_r').val();
                        console.log(pwd_1,pwd_2);
                        if(pwd_1!=pwd_2){
                            $(this).parent().next().find('span').text('密码与第一次输入的不符');
                            flag = false;
                            return false;
                        }
                    }
                    if(!$(':checkbox').prop('checked') && i == 2){
                        $('#user_pwd_r').parent().next().find('span').text('请勾选同意');
                        flag = false;
                        return false;
                    }
                    return flag;
                });

                if(flag){
                    $.ajax({
                        url:'/home/register/',
                        type:'POST',
                        dataType:'json',
                        data:{'user_name':$('#user_name').val(),'user_pwd':$('#user_pwd').val()},
                        success:function(data){
                            if(data.status){
                                alert('账号创建成功，现在跳转到登陆页');
                                location.href = '/home/login'
                            }else {
                                $('#user_name').parent().next().find('span').text(data.message);
                            }
                        }
                    })
                }

            });
        }
    });
})($);