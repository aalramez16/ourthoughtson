function shortCopy(stories){
  for (var i = 0; i < stories.length; i++) {
    var story = stories[i];

    var body = story.body;
    storyId = '#story-' + story.id;
    var copy = body.substr(0,147);
    if (body > copy){
      copy = copy + '...'
    }
    $(storyId).html(copy);
  }
}

function setupGallery(stories,topicData,topics){

  var topic;
  for (var i = 0; i < topics.length; i++) {
    if(topicData.name == topics[i].name)
      topic = topics[i];
  }

  var c0 = $('#col-0');
  var c1 = $('#col-1');
  var c2 = $('#col-2');

  console.log(stories.length);
  console.log(stories);

  for (var i = 0; i < stories.length; i++) {
    story = stories[i]
    storyHref = topicData.url + '/' + story.id;
    console.log(topicData.url);
    console.log(story.id);
    console.log(storyHref);

    var contentWithImage = (
      '<a class="gallery-link" href="' + story.id + '">' +
        '<div class="gallery-item">' +
          '<div class="img-preview"></div>' +
          '<p id="story-' + story.id + '" class="p-with-image">' +
            story.body +
          '</p>' +
        '</div>' +
      '</a>'
    );

    var contentNoImage = (
      '<a class="gallery-link" href="' + story.id + '">' +
        '<div class="gallery-item">' +
          '<p id="story-' + story.id + '">' +
            story.body +
          '</p>' +
        '</div>' +
      '</a>'
    );

    if (i %3 == 0) {
      if (story.img != '') {
        c0.append(contentWithImage);
      }
      else{
        c0.append(contentNoImage);
      }
    }

    if (i %3 == 1) {
      if (story.img != '') {
        c1.append(contentWithImage);
      }
      else{
        c1.append(contentNoImage);
      }
    }

    if (i %3 == 2) {
      if (story.img != '') {
        c2.append(contentWithImage);
      }
      else{
        c2.append(contentNoImage);
      }
    }

  }
}


function populatePreviews(stories){
  var imgs = document.getElementsByClassName("img-preview");
  var imgStories = [];
  for(var i = 0; i < stories.length; i++){
    if(stories[i
    ].img != ''){
      imgStories.push(stories[i]);
    }
  }

  for(var i = 0; i < imgs.length; i++)
  {
    var story = imgStories[i];
    url = "url(/" + story.img + ")";
    imgs[i].style.backgroundImage = url;
  }
}

// $(function(){
//   $('.gallery-item').hover(function(){
//     $('.gallery-item img-preview').addClass('img-preview-is-hover');
//   }, function(){
//     $('.gallery-item img-preview').removeClass('img-preview-is-hover');
//   })
// });
