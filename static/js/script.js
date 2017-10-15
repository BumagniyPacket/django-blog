// novie skripti
$(".search-wrapper").hide();
$(".search-field").focusout(function() {
    $('.search-icon').show();
    $('.search-wrapper').hide();
})

$(".search-icon").click(function() {
    $('.search-icon').hide();
    $('.search-wrapper').show();
    $('.search-field').focus();
})

// fix menu after scrolling
var num = 40; //number of pixels before modifying styles
$(window).bind('scroll', function () {
    if ($(window).scrollTop() > num) {
        $('.menu').addClass('fixed');
    } else {
        $('.menu').removeClass('fixed');
    }
});
