var activeTab = localStorage.getItem('c');

if(activeTab != ""){
  showControlFor(activeTab);
  console.log('this is a smart process');
}
else{
  showControlFor('#notifications');
}

function showControlFor(c){
  $('.admin-menu-item').removeClass('active-item');
  $('.control-item').addClass('hidden');

  if (!$(c).hasClass('active-item')) {
    $(c).addClass('active-item');
  }

  switch (c) {
    case '#notifications':
      $('#notification-hub-container').removeClass('hidden');
      break;
    case '#manageTopics':
      $('#topic-container').removeClass('hidden');
      break;
    case '#registerAdmin':
      $('#admin-form-container').removeClass('hidden');
      break;
  }

  localStorage.setItem('c', c);
  console.log(c);
}
