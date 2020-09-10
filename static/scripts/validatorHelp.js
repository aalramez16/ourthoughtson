doThing = function(){
  var fieldsSmall = document.getElementsByClassName("large-4 medium-6 cell form-space");
  for(var i = 0; i < fieldsSmall.length; i++){
    if (fieldsSmall[i].querySelector('span') != null){
      fieldsSmall[i].querySelector('input').classList.add('is-invalid-input');
      fieldsSmall[i].querySelector('label').classList.add('is-invalid-label');
    }
  }

  var fieldsLarge = document.getElementsByClassName("large-8 medium-12 cell form-space");
  for(var i = 0; i < fieldsLarge.length; i++){
    if (fieldsLarge[i].querySelector('span') != null){
      fieldsLarge[i].querySelector('input').classList.add('is-invalid-input');
      fieldsLarge[i].querySelector('label').classList.add('is-invalid-label');
    }
  }

  var fieldsLarge1 = document.getElementsByClassName("large-12 medium-12 cell form-space");
  for(var i = 0; i < fieldsLarge1.length; i++){
    if (fieldsLarge1[i].querySelector('span') != null){
      fieldsLarge1[i].querySelector('input').classList.add('is-invalid-input');
      fieldsLarge1[i].querySelector('label').classList.add('is-invalid-label');
    }
  }
};


doThing();
