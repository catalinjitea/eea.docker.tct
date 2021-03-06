$(document).ready(function() {


   

    if (window.matchMedia("(min-width: 800px)").matches) {
   setTimeout(function() {
        $('.homepage-info').fadeTo("fast", 1);
    setTimeout(function() {
        $('.homepage-info').removeClass('info-translated')
        setTimeout(function() {
            $('.content .trigger-overlay').fadeTo("fast", 1);
        }, 1500);
    }, 500);
  }, 500);
} else {
    $('.homepage-info').fadeTo("fast", 1);
    $('.homepage-info').removeClass('info-translated');
    $('.homepage-info').css('left','0');
    $('.content .trigger-overlay').fadeTo("fast", 1);
}


    $(".overlay").prependTo("body");
    $trigger = $('.trigger-overlay');
    $overlay = $('.overlay');
    $close = $('.overlay-close');
    $container = $('.container');

    $trigger.on('click', function() {
        $('body').addClass('no-ovf');
        $overlay.addClass('display').delay(1).queue(function() {
            $overlay.addClass('open');
            $container.addClass('overlay-open');
            $overlay.dequeue();
            $container.dequeue();
        });
    })

    $close.on('click', function() {
        $('body').removeClass('no-ovf');
        $overlay.removeClass('open').delay(500).queue(function() {
            $overlay.removeClass('display');
            $overlay.dequeue();

        });
        $container.removeClass('overlay-open');
    })

});
