$(document).ready(function() {
    $(".food_id").each(function(i) {
        var foodid = $(this).html();
        var given_fav = $(this);
        $.ajax({
            type: "GET",
            data: { foodid: foodid },
            url: "/check_favorites"
        }).done(function(favorites_exist) {
            if (favorites_exist == "favorites_exist") {
                $(given_fav).siblings().children("#favorite-span").children().children().css('color', 'red');
            }
        });
    });

    var add_favorites_btn = $(".add_favorites_btn");
    $(add_favorites_btn).click(function(e) {
        var pathname = window.location.pathname;
        var clicked_fav = $(this);
        var foodid = $(this).parent().parent().siblings(".food_id").html();
        $.ajax({
            type: "GET",
            data: { foodid: foodid },
            url: "/add_favorites"
        }).done(function(favorites_exist) {
            var number_of_favorites = favorites_exist.slice(9);;
            if (favorites_exist.includes("favorites")) {
                $(clicked_fav).children().css('color', 'pink');
                $(clicked_fav).siblings("span").html(number_of_favorites);
                if (pathname == "/my_favorites") {
                    window.location.reload();
                }
            }
            else if (favorites_exist.includes("favorinot")) {
                $(clicked_fav).children().css('color', 'red');
                $(clicked_fav).siblings("span").html(number_of_favorites);
            }
        });
    });
});
