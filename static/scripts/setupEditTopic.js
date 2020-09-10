$("body").on('change', '#edit-topic-select', updateSelect);
$("body").on('input', '#edit-topic-input', updateInput);
//document.getElementById('edit-topic-input').addEventListener("input", updateName());

$("body").on('change', '#edit-topic-select', setupColors);
$("body").on('change','#edit-topic-select', updateEditColor);
$("body").on('change', '#edit-color-input', function(){
  newColor = document.getElementById('edit-color-input').value;
  $('#edit-topic-preview').css({'border-left-style':'solid', 'border-left-width':'8px', 'border-left-color':newColor});
});


var topicNames = [];
var topicColors = [];
var color;
function getTopics(t){
  for (var i = 0; i < t.length; i++) {
    topicNames[i] = t[i].name;
    topicColors[i] = t[i].color;
  }
}

function updateEditColor(){
  newColor = document.getElementById('edit-topic-input').value;
  $('#edit-topic-preview').css({'border-left-style':'solid', 'border-left-width':'8px', 'border-left-color':color});
  if(newColor == ''){
    $('#edit-topic-preview').css({'border-left-style':'solid', 'border-left-width':'8px', 'border-left-color':'#999999'});
  }
}

function setupColors(){
  var topic;
  var topicValue = document.getElementById('edit-topic-select').value;
  for (var i = 0; i < topicNames.length; i++) {
    if(topicValue == topicNames[i]){
      color = topicColors[i];
    }
  }
  updateEditColor();
  document.getElementById('edit-color-input').value = color;
  $('#edit-color-input').css({'background-color':color});

}


function updateSelect(){
  var topicValue = document.getElementById('edit-topic-select').value;
  document.getElementById('edit-topic-input').value = topicValue;
  document.getElementById('reference-input').value = topicValue;
  document.getElementById('edit-topic-contents').innerHTML = topicValue;
  setupColors();
}

function updateInput(){
  var previewContents = document.getElementById('edit-topic-contents');
  name = document.getElementById('edit-topic-input').value;
  previewContents.innerHTML = name;
  if(name == ''){
    previewContents.innerHTML = 'Preview';
  }
}
