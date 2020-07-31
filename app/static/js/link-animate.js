$(window).bind("pageshow", () => {
    $(".padding-header").css("height", $("header").height());
    $("main.content").addClass("show");
});

$(function() {
    $("a.internal-link").click(function(e) {
        var evt = window.evt || e;
        evt.preventDefault();
        $(".nav-curr").animate({bottom: "-=0.2rem"}, {duration: 200, queue: false});
        if ($(evt.target).parent().is($(".nav-item"))) {
            $(evt.target).parent().toggleClass("hovered");
        }
        $("main.content").removeClass("show");
        setTimeout(function() {
            window.location.href = $(evt.target).attr("href");
        }, 200);
    })
});