var getStory = function(stories, indx){
  var story = stories[indx];
  $('#story').html(story.body);
  return(story);
};

function imgResize(){
var imgWidth = $('.story-img').outerWidth();
var ratio = (4/3);
$('.story-img').css("height",function() {
  return imgWidth * ratio;
});
}

function storyPopulate(story){

  var hasImg = function(story){
    if(story.img!=''){
      return true;
    }
    else{
      return false;
    }
  }

  var imgUrl = "/../../" + story.img;

  console.log(story.img);

  const imgResizer = new Vue({
    el: '#story-container',
    data: {
      hasImg: hasImg(story),
      imgUrl: imgUrl
    }
  });

  window.addEventListener('resize', imgResize);
}
