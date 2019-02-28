$(document).ready(function() {
    $(".food-name").each(function(i) {
        var foodname = $(this).html().toLowerCase();
        var given_fav = $(this);
        $.ajax({
            type: "GET",
            data: { foodname: foodname },
            url: "/check_favorites"
        }).done(function(favorites_exist) {
            if (favorites_exist == "favorites_exist") {
                $(given_fav).siblings().children("#favorite-span").children().children().css('color', 'red');
            }
        });
    });

    var add_favorites_btn = $(".add_favorites_btn");
    $(add_favorites_btn).click(function(e) {
        var clicked_fav = $(this);
        var foodname = $(this).parent().parent().siblings("h2").html().toLowerCase();
        $.ajax({
            type: "GET",
            data: { foodname: foodname },
            url: "/add_favorites"
        }).done(function(favorites_exist) {
            console.log(favorites_exist)
            var number_of_favorites = favorites_exist.slice(9);;
            if (favorites_exist.includes("favorites")) {
                $(clicked_fav).children().css('color', 'pink');
                $(clicked_fav).siblings("span").html(number_of_favorites);
                window.location.reload();
            }
            else if (favorites_exist.includes("favorinot")) {
                $(clicked_fav).children().css('color', 'red');
                $(clicked_fav).siblings("span").html(number_of_favorites);
            }
        });
    });
});
