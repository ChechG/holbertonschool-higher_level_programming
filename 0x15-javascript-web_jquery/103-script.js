$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const str = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + str, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === '13') {
      const str1 = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + str1, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
