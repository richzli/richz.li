$(window).bind("pageshow", () => { $(".ml").fadeIn(1000); });

$(function() {
    $(".ml-away").click(function(e) {
        var evt = window.event || e;
        evt.preventDefault();
        $(".ml").fadeOut(500);
        setTimeout(function() {
            window.location.href = $(evt.target).attr("href");
        }, 500);
    });
});