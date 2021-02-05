
$(document).ready(function () {
    $('a[href^="#"]').click(function () {
        var destiny = $(this.hash);
        if (destiny.length == 0) {
            destiny = $('a[name="' + this.hash.substr(1) + '"]');
        }
        if (destiny.length == 0) {
            destiny = $('html');
        }
        $('html, body').animate({ scrollTop: destiny.offset().top }, 500);
        return false;
    });
});

$(document).ready(function () {
    "use strict";

    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });

    // scroll body to 0px on click
    $("#back-to-top").on("click", function () {
        $('body,html').animate({
            scrollTop: 0
        }, 200);
        return false;
    });
});
