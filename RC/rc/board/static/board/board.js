function ctl_cookie(board_type){
    var getCookie = function(name) {
      var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
      return value? value[2] : null;
    };
    var setCookie = function(name, value, exp) {
      var date = new Date();
      date.setTime(date.getTime() + exp*24*60*60*1000);
      document.cookie = name + '=' + value + ';expires=' + date.toUTCString() + ';path=/';
    };
    var deleteCookie = function(name) {
      document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    deleteCookie('current_board')

    setCookie('current_board', board_type, 7)
    return getCookie('current_board')
}

function ctl_btn_by_board_type(board_type){
    if( board_type == 1 ){
        $("#btn_board_type_1").css({'background-color': 'white'})
        $("#btn_board_type_2").css({'background-color': 'white'})
        $("#btn_board_type_1").css({'background-color': '#71c55d'})
        $("#btn_board_type_1").css({'color': 'white'})
    }
    if( board_type == 2 ){
        $("#btn_board_type_1").css({'background-color': 'white'})
        $("#btn_board_type_2").css({'background-color': 'white'})
        $("#btn_board_type_2").css({'background-color': '#71c55d'})
        $("#btn_board_type_2").css({'color': 'white'})
    }
}