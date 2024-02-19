// slick slider
$('.slick-slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  dots:true,
  autoplaySpeed: 2000,
});
$('.menu-row').slick({
  slidesToShow: 3,
  slidesToScroll: 3,
  autoplay: false,
  dots:false,
  autoplaySpeed: 2000,
});

// header fixed
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 850) {
        $("header").addClass("fix");
    } else {
        $("header").removeClass("fix");
    }
});