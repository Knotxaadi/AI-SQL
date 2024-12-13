$(document).ready(function() {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp"
        },
        out: {
            effect: "fadeOutDown"
        }
    })
});