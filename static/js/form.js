// content preview
var contentInput = $("#id_content");
function setContent(value) {
    var markedContent = marked(value);
    $("#preview-content").html(markedContent);
    $("#preview-content img").each(function () {
        $(this).addClass("img-responsive");
    });
}
setContent(contentInput.val());
contentInput.keyup(function () {
    var newContent = $(this).val();
    setContent(newContent);
});
var titleInput = $("#id_title");

function setTitle(value) {
    $("#preview-title").text(value);
}
setTitle(titleInput.val());
titleInput.keyup(function () {
    var newContent = $(this).val();
    setTitle(newContent);
});
// end content preview

//change input height
function h() {
    $(this).css({'height':'auto','overflow-y':'hidden'}).height(this.scrollHeight);
}
$(document).on('input', 'textarea', h).trigger('input');
// end change input height