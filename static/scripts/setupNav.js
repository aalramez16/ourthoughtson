var isMobile = false;
var isDesktop = true;

const navSelector = new Vue({
  el: '#menu',
  data: {
    isMobile: isMobile,
    isDesktop: isDesktop
  }
});

if (navigator.appName == 'Microsoft Internet Explorer' || navigator.appName == 'Microsoft Internet Explorer') {
  $('search').addClass('ms-search');
}
