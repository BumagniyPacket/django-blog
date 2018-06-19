function render_article(data){
    var title = data['title']
    var url = data['url']
    var description = data['description']
    var timestamp = data['timestamp']
    var image = data['image']

    $(".articles").append(
        `
        <div class="article">
            <div class="article__image">
                <img src="${image}">
            </div>
            <div class="article__description">
                <a href="${url}">
                    <p class="article__title">${title}</p>
                </a>
                <p class="article__date">${timestamp} назад</p>
            </div>
        </div>
        `
    )
}

function render_next_button(data) {
    if ( data ) {
        $(".btn__next").append(
            "<div id=\"btn__next__data\" url=" + data + "><p class=\"next_page\">Загрузить еще</p></div>"
        )
    }
}

function render_list(json) {
    var next = json["next"];
    var articles = json["results"];

    for (var article in articles) {
        render_article(articles[article]);
    }
    render_next_button(next);
}

function get_articles_list(url) {
    if (url === undefined) {
        url = "/api/v1/article/";
    }
    $.ajax({
        url: url,
        type: "GET",
        datatype: "json",
        success: function(json){
            render_list(json);
        },
        error: function(json){
            alert("ERROR");
        }
    });
}

$(document).ready(get_articles_list());
$( ".btn__next" ).click(function() {
    url = $("#btn__next__data").attr("url")
    $("#btn__next__data").remove()
    get_articles_list(url)
});