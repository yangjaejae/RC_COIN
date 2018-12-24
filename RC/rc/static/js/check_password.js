function modal_toggle() {
    $("#myModal").modal("show");
}

function login_failed() {
    console.log('err');
    if ($("#status").val() == "failed") {
        return true;
    }
}

$(function() {
    if (login_failed() ) {
        modal_toggle();
    }
})