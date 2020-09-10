document.getElementById('topic-name-input').setAttribute('oninput', 'updateName()');
document.getElementById('topic-color-input').setAttribute('value', '#999999');
document.getElementById('topic-color-input').setAttribute('onchange', 'updateColor()');
document.getElementById('topic-color-input').setAttribute('oninput', 'updateColor()');

function updateName(){
  var previewContents = document.getElementById('preview-contents');
  var name = document.getElementById('topic-name-input').value;
  previewContents.innerHTML = name;
  if(name == ''){
    previewContents.innerHTML = 'Preview';
  }
}

function updateColor(){
  var color = document.getElementById('topic-color-input').value;
  $('#topic-preview').css({'border-left-style':'solid', 'border-left-width':'8px', 'border-left-color':color});
  if(color == ''){
    $('#topic-preview').css({'border-left-style':'solid', 'border-left-width':'8px', 'border-left-color':'#999999'});
  }
}
