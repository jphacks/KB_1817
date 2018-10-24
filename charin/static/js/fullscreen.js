function () {
    sizing();
    $(window).resize(function() {
        sizing();
    });
});

function sizing(){
    $("#main").attr({height:$("#wrapper").height()});
    $("#main").attr({width:$("#wrapper").width()});
}
