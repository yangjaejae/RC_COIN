var email_validated = false;

function modal_toggle() {
    $("#myModal").modal("show");
}

function check_validate() {
    var email = $("#email").val();
    var regex = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
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
    email_validated = true;
}

function find_username() {
    var email = $("#email").val();
    $.ajax({
        type: "GET",
        url: "getUserList/",
        data: {
            email : email
        },
        dataType : "json",
        async: false,
        success: function(data) {
            if( data["user_list"] ){
                let user_list = data["user_list"];
                let result = "";
                if (user_list.length > 0) {
                    for (let i = 0; i < user_list.length; i++) {
                        result += `<ul>${user_list[i]}</ul>`;
                    }
                    $("#msg").append(result);
                    $("#msg > ul").css({
                        fontSize: "20px",
                        color: "#1d2124",
                        fontWeight: "bold"
                    });
                } else {
                    $("#msg").text("검색결과가 없습니다.");
                    $("#msg").css({
                        fontSize: "20px",
                        color: "#ff3434"
                    });
                }
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
        if (email_validated) {
            find_username();
        }
        modal_toggle();
    });
})