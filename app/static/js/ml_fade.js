$(window).bind("pageshow", () => { $("main").fadeIn(500); });

$(function() {
    $(".ml-away").click(function(e) {
        var evt = window.event || e;
        evt.preventDefault();
        $("main").fadeOut(500);
        setTimeout(function() {
            window.location.href = $(evt.target).attr("href");
        }, 1000);
    });
});