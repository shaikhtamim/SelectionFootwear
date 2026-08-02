$(document).ready(function () {
    var $slider = $(".testimonial-slider");
    var count = $slider.find('.review-card').length;

    if (!count) {
        return;
    }

    $slider.owlCarousel({
        items: 3,
        loop: count > 3,      // Enables loop if more than 3 items exist
        margin: 24,
        nav: false,
        dots: true,
        autoplay: count > 1,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        smartSpeed: 600,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {           // Exact 3 items per row for standard laptop/desktop screens
                items: 3
            }
        }
    });

    $("#reviewPrevBtn").on("click", function () {
        $slider.trigger("prev.owl.carousel");
    });

    $("#reviewNextBtn").on("click", function () {
        $slider.trigger("next.owl.carousel");
    });
});