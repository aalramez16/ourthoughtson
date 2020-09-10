var table = $('#notificationsTable tbody');

var size = 0;
var names = [];
var emails = [];
var dates = [];
var suggestions = [];
var messages = [];
var notificationIDs = [];
var activeId;
function getNotificationData(n){
  size=n.length;
  if (n.length != 0) {
    n.sort((a, b) => b.ID - a.ID);
    for(var i = 0; i < n.length; i++){
      names[i]=n[i].name;
      emails[i]=n[i].email;
      dates[i]=n[i].date;
      suggestions[i]=n[i].topic_submission;
      messages[i]=n[i].topic_explain;
      notificationIDs[i]=n[i].ID;
    }
  }
  console.log(messages);
  console.log(names);
}

function populateNotifications(){
  if (size == 0) {
    table.append(
      '<tr>' +
        '<td>No notifications to show</td>' +
      '</tr>'
    );
  } else {

    for(var i = 0; i < size; i++){
      if (names[i] == '') {
        names[i] = 'Anonymous';
      }
      if (messages[i] == ''){
        messages[i] = 'No Description to show.';
      }
      table.append(

        '<tr id="' + notificationIDs[i] + '">' +
          '<td>' + '<a href="javascript:Void(0)">' + 'Topic Suggestion From <br>' + names[i] + '</a>' + '</td>' +
          '<td>' + '<span class="notification-date">' + dates[i] + '</span>' + '</td>' +
          '<td>' + '<button class="button dismiss-notification">' + '×' + '</button>' + '</td>' +
        '</tr>'
      );
    }
    $(("#"+notificationIDs[0])).addClass('notification-active');
    loadNotificationDetails(notificationIDs[0]);
  }
}

var detailContent = $('#detail-content');

$(document).ready(function() {
  $("#notificationsTable tr").click(function(event) {

      activeId=this.id;
      activeIdString = "#" + activeId;
      console.log(activeIdString);
      $("#notificationsTable tr").removeClass('notification-active');
      $(activeIdString).addClass('notification-active');
      console.log($(activeIdString).hasClass('notification-active'));

      loadNotificationDetails(activeId);
  });
});

function loadNotificationDetails(activeId){
  var nNid = parseInt(activeId);
  var index;
  for (var i = 0; i < size; i++) {
    if (notificationIDs[i] == nNid) {
      index = i;
    }
  }
  detailContent.html(
    '<p>' +
      'From ' + '<strong>' + names[index] + '</strong>' + ' at ' +
      '<a href="mailto:' + emails[index] + '">' + emails[index] + '</a>' + ':' +
    '</p>' +
    '<p>' +
      'Topic: ' + '<strong>' + suggestions[index] + '</strong>' +
      '<br />' +messages[index] +
    '</p>'
  );
}
