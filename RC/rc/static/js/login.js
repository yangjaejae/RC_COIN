var isValidated = false;

function modal_setMsg(msg) {
    $("#msg").text(msg);
}

function modal_toggle() {
    $("#myModal").modal("show");
}

function check_validate() {
    var username = $("#username").val();
    var password = $("#password").val();
    if (username.length < 1) {
        modal_setMsg("아이디는 필수 입력 항목입니다.");
        modal_toggle();
        return false;
    } else if (password.length < 1) {
        modal_setMsg("비밀번호는 필수 입력 항목입니다.");
        modal_toggle();
        return false;
    }
    return true;
}

function login_failed() {
    if ($("#status").val() == "failed") {
        modal_setMsg("아이디 또는 비밀번호가 올바르지 않습니다.");
        modal_toggle();
    }
}

$(function() {
    login_failed();
})