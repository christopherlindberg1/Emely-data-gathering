

// Smooth scroll on nav click
$(".nav-link, .navbar-brand, .link-scroll").on("click", function(e) {
    try {
        if (this.hash !== "") {
            e.preventDefault();
            const hash =  this.hash;
            $("html, body").animate({
                scrollTop: $(hash).offset().top - 56
            }, 0);
        }
    }
    catch (ex) {
        if (e.target.innerText == "About me") {
            window.location = "./../#section-about";
        } else if (e.target.innerText == "Projects") {
            window.location = "./../#section-projects";
        }
    }
});

// Close menu links on link click
$(function(){ 
    var navMain = $(".navbar-collapse");
    navMain.on("click", "a:not([data-toggle])", null, function () {
        navMain.collapse('hide');
    });
});

// Close menu when clicking outside of it
document.getElementById("main").addEventListener("click", e => {
    var navMain = $(".navbar-collapse");
    navMain.collapse('hide');
});