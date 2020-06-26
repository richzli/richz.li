$(window).bind("pageshow", () => {
    $("main").fadeIn(500);
    $("main").particleground({
        dotColor: "#D0D0D0",
        lineColor: "#D0D0D0",
        density: 14000,
        parallax: false
    });
});

$(function() {
    $(".ml-away").click(function(e) {
        var evt = window.event || e;
        evt.preventDefault();
        $("main").fadeOut(500);
        setTimeout(function() {
            window.location.href = $(evt.target).attr("href");
        }, 500);
    });
});