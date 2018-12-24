var validated = false;

function modal_toggle() {
    $("#myModal").modal("show");
}

function check_validate() {
    var username = $("#username").val();
    var email = $("#email").val();
    var regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
    if (username.length < 1) {
        $("#msg").text("아이디를 입력해주세요.");
        $("#msg").css({
            fontSize: "20px",
            color: "#ff3434"
        });
        return;
    }
    if (email.length < 1) {
        $("#msg").text("이메일을 입력해주세요.");
        $("#msg").css({
            fontSize: "20px",
            color: "#ff3434"
        });
        return;
    } else if (email.match(regex) == null) {
        $("#msg").text("이메일 형식이 잘못되었습니다.");
        $("#msg").css({
            fontSize: "20px",
            color: "#ff3434"
        });
        return;
    }
    validated = true;
}

function init_password() {
    var username = $("#username").val();
    var email = $("#email").val();
    $.ajax({
        type: "GET",
        url: "initPassword/",
        data: {
            username : username,
            email : email
        },
        dataType : "json",
        async: false,
        success: function(data) {
            if ( data["result"] ){
                $("#msg").text("임시 비밀번호를 등록된 이메일로 발송했습니다.");
                $("#msg").css({
                    fontSize: "20px",
                    color: "#1d2124",
                    fontWeight: "bold"
                });
            } else {
                $("#msg").text("아이디 또는 이메일 주소가 올바르지 않습니다.");
                $("#msg").css({
                    fontSize: "20px",
                    color: "#ff3434"
                });
            }
        },
        error: function( jqXHR, textStatus, errorThrown ){
                alert("status: " + textStatus + "\nerror: " + jqXHR.error );
        }
    });
}

$(function() {
    $(".submitButton").click(function () {
        $("#msg").empty();
        check_validate();
        if (validated) {
            init_password();
        }
        modal_toggle();
    });
})