
$(function() {

    $("#username").keyup( function(event) {
        $("#msg").text("사용자정보를 입력해주세요.").attr('class', 'alert alert-success');
    });

    $("#password").keyup( function(event) {
        $("#msg").text("사용자정보를 입력해주세요.").attr('class', 'alert alert-success');
    });

    $("#btn_login").click( function(event) {
        var username = $("#username").val();
        var password = $("#password").val();

        if( username == "" ) {
            $("#msg").text("아이디를 입력하세요.").attr('class', 'alert alert-danger');
        } else if( password == "" ) {
            $("#msg").text("비밀번호를 입력하세요.").attr('class', 'alert alert-danger');
        } else {
            $("#signup").submit();
        }

        return false;
    });

})