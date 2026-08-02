$(document).ready(function () {

    var $slider = $(".category-slider");
    var count = $slider.children().length;

    if (!count) {
        return;
    }

    $slider.owlCarousel({

        // Fixed slot sizes so few products don't stretch. Loop only when 5+.
        loop: count > 4,

        margin: 25,

        nav: false,

        dots: count > 4,

        dotsEach: 1,

        slideBy: 1,

        autoplay: count > 4,

        autoplayTimeout: 2000,

        autoplayHoverPause: false,

        smartSpeed: 800,

        responsive: {

            0: {
                items: 1
            },

            576: {
                items: 2
            },

            768: {
                items: 3
            },

            992: {
                items: 4
            },

            1200: {
                items: 4
            }
        }

    });

});
