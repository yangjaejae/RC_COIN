function setSelectForYear() {
    var myYear = $("#_birth_year").val();
    var toYear = new Date().getFullYear();

    for(var year=toYear; year>=1900; year--) {
        var option = "<option value='" + year + "'>" + year + "</option>";
        $("#birth_year").append(option);
    }

    if( myYear ) {
        $("#birth_year").val(myYear).prop("selected", true);
    }
}

function setSelectForMonth() {
    var myMonth = $("#_birth_month").val();
    var toMonth = new Date().getMonth();

    for(var month=1; month<=12; month++) {
        var option = "<option value='" + month + "'>" + month + "</option>";
        $("#birth_month").append(option);
    }

    if( myMonth ) {
        $("#birth_month").val(myMonth).prop("selected", true);
    }
}

function setSelectForDate() {
    var myDate = $("#_birth_date").val();
    var toDate = new Date().getDate();

    for(var month=1; month<=31; month++) {
        var option = "<option value='" + month + "'>" + month + "</option>";
        $("#birth_date").append(option);
    }

    if( myDate ) {
        $("#birth_date").val(myDate).prop("selected", true);
    }
}

function selectGender() {
    var myGender = $("#_gender").val();

    if( myGender ) {
        $("#gender").val(myGender).prop("selected", true);
    }
}


// onload

$(function () {
    setSelectForYear();
    setSelectForMonth();
    setSelectForDate();
    selectGender()

    if( $("#_gender").val() && $("#_birth_year").val() ) {
        isValidUsername = true;
    }
});


// validation check

var isValidUsername = false;
var isValidPassword1 = false;
var isValidPassword2 = false;


$("#username").keyup(function (event) {

    $("#formErrorMsg").empty();

    var pattern = /^[a-zA-Z0-9]*$/g;

    if( $("#username").val() == "") {
        $("#usernameErrorMsg").empty();
        isValidUsername = false;
    } else if( $("#username").val().length < 4 ||  $("#username").val().length > 20 )  {
        $("#usernameErrorMsg").text("아이디는 '4 이상 20 이하'의 길이만 가능합니다.").css("color", "#d84461");
        isValidUsername = false;
    } else if( !$("#username").val().match(pattern) ) {
        $("#usernameErrorMsg").text("아이디는 알파벳 대소문자, 숫자만 사용 가능합니다.").css("color", "#d84461");
        isValidUsername = false;
    } else {
        $("#usernameErrorMsg").empty();
        isValidUsername = true;
    }
});

$("#password1").keyup(function (event) {

    $("#formErrorMsg").empty();

    var pattern = /^.*(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$]).*$/;

    if ( $("#password1").val().length < 8 )  {
        $("#pwdErrorMsg1").text("비밀번호는 8자 이상의 길이이어야 합니다.").css("color", "#d84461");
        isValidPassword1 = false;
    } else if( !pattern.test($("#password1").val()) ) {
        $("#pwdErrorMsg1").text("비밀번호는 알파벳 대소문자, 숫자, 특수문자(!@#$)를 최소 하나씩 포함해야합니다.").css("color", "#d84461");
        isValidPassword1 = false;
    } else if ( ( $("#username").val().length != 0 ) &&
            ( $("#password1").val().includes($("#username").val()) || $("#username").val().includes($("#password1").val()) ) ) {
        $("#pwdErrorMsg1").text("아이디와 유사한 비밀번호는 사용할 수 없습니다.").css("color", "#d84461");
        isValidPassword1 = false;
    } else {
        $("#pwdErrorMsg1").empty();
        isValidPassword1 = true;
    }
});

function invalidCheckPwd2() {
    $("#formErrorMsg").empty();
    if ( $("#password1").val() != $("#password2").val() )  {
        $("#pwdErrorMsg2").text("비밀번호가 일치하지 않습니다.").css("color", "#d84461");
        isValidPassword2 = false;
    } else if ( $("#password1").val().length == 0 ) {
        $("#pwdErrorMsg2").empty();
        isValidPassword2 = false;
    } else {
        $("#pwdErrorMsg2").text("비밀번호 일치").css("color","#00c73c");
        isValidPassword2 = true;
    }
}

$("#password1").keyup(invalidCheckPwd2);
$("#password2").keyup(invalidCheckPwd2);


$("#btn_submit").click(function (event) {
    var username = $("#username").val();

    if( isValidUsername && $("#_gender").val() == "" ) {
        $.ajax({
            type: "GET",
            url: "check_username/",
            data: {
                username : username
            },
            dataType : "json",
            async: false,
            success: function(data) {
                if( data["result"] ){
                    $("#usernameErrorMsg").text("이미 등록된 아이디 입니다.").css("color", "#d84461");
                    isValidUsername = false;
                    return false;
                }
            },
            error: function( jqXHR, textStatus, errorThrown ){
                    alert("status: " + textStatus + "\nerror: " + jqXHR.error )
                    isValidUsername = false;
                    return false;
            }
        });
    }

    if( isValidUsername && isValidPassword1 && isValidPassword2 ){
        $("#register").submit();
    } else {
        $("#formErrorMsg").text("입력 정보가 올바르지 않습니다").css("color", "#d84461");
        return false;
    }
});