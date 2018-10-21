$(document).ready(function() {
    $("#open").on("click", function(e) {
        e.preventDefault();
        $("#overlay, #modal").addClass("active");

        $("#close, #overlay").on("click", function() {
            $("#overlay, #modal").removeClass("active");
            return false;
        });
    });
});