$(document).ready(function() {
    var add_favorites_btn = $(".add_favorites_btn");
    $(add_favorites_btn).click(function(e) {
        var clicked_fav = $(this);
        var foodname = $(this).parent().parent().siblings("h2").html().toLowerCase();
        $.ajax({
            type: "GET",
            data: { foodname: foodname },
            url: "/add_favorites"
        }).done(function(favorites_exist) {
            if (favorites_exist == "favorites_exist") {
                 $(clicked_fav).children().css('color', 'blue');
            }
            else if (favorites_exist == "") {
                $(clicked_fav).children().css('color', 'pink');
            }
        });
    });
});
