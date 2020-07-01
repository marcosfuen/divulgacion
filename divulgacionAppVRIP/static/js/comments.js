$(document).ready(function () {
    $('.reply-btn').click(function() {
        $(this).parent().next('.reply-comments').fadeToggle()
    });
});