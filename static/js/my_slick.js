//This script is responsible for the carousel what shows the cuisines on the home page
$(document).ready(function() {
    $(".carousel").slick({
        arrows: true,
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 5,
        swipeToSlide: true,
        centerMode: true,
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3
            }
        }],
    });
});
