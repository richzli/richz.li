$(window).bind("pageshow", () => { $("main").fadeIn(500); });

$(function() {
    $(".nav-item a").click(function(e) {
        var evt = window.event || e;
        evt.preventDefault();
        $(".nav-curr").animate({bottom: "-=0.2rem"}, {duration: 500, queue: false});
        $(evt.target).parent().toggleClass("hovered");
        $("main").fadeOut(500);
        setTimeout(function() {
            window.location.href = $(evt.target).attr("href");
        }, 500);
    });
});