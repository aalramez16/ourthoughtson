$(document).click(function(event) {
  if(!$(event.target).closest('#menu').length) {
      if(!(document.getElementById("mobDropdown").classList.contains('hidden'))) {
        document.getElementById("mobDropdown").classList.add('hidden')
        document.getElementById("icon-menu").classList.remove('menu-active');
      }
  }
});
