$( '.contributors img[data-src]' ).each( function() {
    src = $(this).attr("data-src");
    $(this).attr('src',src);
});