$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').replaceWith('<div id="character">' + data.name + '</div>');
  });
});
