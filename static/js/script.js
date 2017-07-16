$(document).ready(function () {
  $(".content-markdown").each(function () {
    var content = $(this).text();
    // console.log(content);
    var markedContent = marked(content);
    // console.log(markedContent);
    $(this).html(markedContent);
  });
  $(".content-markdown img").each(function () {
    var content = $(this).text();
    // console.log(content);
    var markedContent = marked(content);
    // console.log(markedContent);
    $(this).html(markedContent);
  })
});

//back to top
$(function () {
  $.fn.scrollToTop = function () {
    $(this).hide().removeAttr("href");
    if ($(window).scrollTop() != "0") {
      $(this).fadeIn("slow")
    }
    var scrollDiv = $(this);
    $(window).scroll(function () {
      if ($(window).scrollTop() == "0") {
        $(scrollDiv).fadeOut("slow")
      } else {
        $(scrollDiv).fadeIn("slow")
      }
    });
    $(this).click(function () {
      $("html, body").animate({scrollTop: 0}, "slow")
    })
  }
});

$(function () {
  $("#toTopWrapper").scrollToTop();
});

var contentInput = $("#id_content");
function setContent(value) {
  var markedContent = marked(value)
  $("#preview-content").html(markedContent)
  $("#preview-content img").each(function () {
    $(this).addClass("img-responsive")
  })
}
setContent(contentInput.val())
contentInput.keyup(function () {
  var newContent = $(this).val()
  setContent(newContent)
})
var titleInput = $("#id_title");

function setTitle(value) {
  $("#preview-title").text(value)
}
setTitle(titleInput.val())
titleInput.keyup(function () {
  var newContent = $(this).val()
  setTitle(newContent)
})