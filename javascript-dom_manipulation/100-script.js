window.addEventListener('DOMContentLoaded', function() {
  const list = document.querySelector('.my_list');

  document.getElementById('add_item').addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    list.appendChild(li);
  });

  document.getElementById('remove_item').addEventListener('click', function() {
    const items = list.querySelectorAll('li');
    if (items.length > 0) {
      list.removeChild(items[items.length - 1]);
    }
  });

  document.getElementById('clear_list').addEventListener('click', function() {
    list.innerHTML = '';
  });
});