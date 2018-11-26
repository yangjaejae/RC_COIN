function setCategory() {
    var myCategory = $("#myCategory").val();

    $("#category option:eq(1)").prop("selected", true);

    if( myCategory != null && myCategory != "") {
        $("#category").val(myCategory).prop("selected", true);
    }
}

function setLocation() {
    var myLocation = $("#myLocation").val();

    $("#location option:eq(1)").prop("selected", true);

    if( myLocation != null && myLocation != "") {
        $("#location").val(myLocation).prop("selected", true);
    }
}

function setTime() {
    var myOpening_hour = $("#myOpening_hour").val();
    var myOpening_minute = $("#myOpening_minute").val();
    var myClosing_hour = $("#myClosing_hour").val();
    var myClosing_minute = $("#myClosing_minute").val();

    for( var i=0; i<24; i++ ) {
        var ii = i >= 10 ? i : '0' + i.toString();
        var option = '<option value="' + ii + '">' + ii + '</option>';
        $("#opening_hour").append(option);
        $("#closing_hour").append(option);
    }

    for( var i=0; i<60; i++ ) {
        var ii = i >= 10 ? i : '0' + i.toString();
        var option = '<option value="' + ii + '">' + ii + '</option>';
        $("#opening_minute").append(option);
        $("#closing_minute").append(option);
    }

    $("#opening_hour").val("00").prop("selected", true);
    $("#opening_minute").val("00").prop("selected", true);
    $("#closing_hour").val("00").prop("selected", true);
    $("#closing_minute").val("00").prop("selected", true);

    if( myOpening_hour != "None") {
        $("#opening_hour").val(myOpening_hour).prop("selected", true);
        $("#opening_minute").val(myOpening_minute).prop("selected", true);
        $("#closing_hour").val(myClosing_hour).prop("selected", true);
        $("#closing_minute").val(myClosing_minute).prop("selected", true);
    }
}

$(function() {
    setCategory();
    setLocation();
    setTime();

    $("#btn_modify").click(function(event) {
        var name = $("#name").val();
        var corporate_number = $("#corporate_number").val();
        var description = $("#description").val();
        var pattern = /^\d{3}-\d{2}-\d{5}$/;

        if( name == "" ) {
            $("#msg").text('상호명을 입력해주세요.').attr('class', 'alert alert-danger');
        } else if( corporate_number == "" ) {
            $("#msg").text('사업자등록번호를 입력해주세요.').attr('class', 'alert alert-danger');
        } else if( !corporate_number.match(pattern) ) {
            $("#msg").text('사업자등록번호가 올바르지 않습니다.').attr('class', 'alert alert-danger');
        } else if( description == "" ) {
            $("#msg").text('가맹점 설명을 입력해 주세요.').attr('class', 'alert alert-danger');
        } else {
            $("#edit_form").submit();
        }

        return false;
    });
})