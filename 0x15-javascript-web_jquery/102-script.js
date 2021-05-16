$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const str = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + str, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
