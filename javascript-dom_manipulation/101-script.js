window.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn_translate').addEventListener('click', function() {
    const lang = document.getElementById('language_code').value;

    fetch('https://hellosalut.stefanbohacek.com/?lang=' + lang)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        document.getElementById('hello').textContent = data.hello;
      });
  });
});