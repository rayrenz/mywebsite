$(document).ready(function(){
    $(".search").keyup(function(){
        myFunction();
    });
});

function myFunction() {
    var thumbnails = $(".album");
    var filter = $(".search").val().toLowerCase();

    $.each(thumbnails, function(){
        var a = $(this).find("a").text().toLowerCase() + $(this).find("h5").text().toLowerCase();
        if (a.indexOf(filter) > -1) {
            $(this).css("display", "initial");
        } else {
            $(this).css("display", "none");
        }
    });

}