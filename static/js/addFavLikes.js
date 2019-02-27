$(document).ready(function() {
    var add_favorites_btn = $(".add_favorites_btn");
    $(add_favorites_btn).click(function(e) {
        var foodname = $(this).parent().parent().siblings("h2").html().toLowerCase();
        $.ajax({
            type: "GET",
            data: {foodname : foodname},
            url: "/add_favorites"
        });
    });
});
