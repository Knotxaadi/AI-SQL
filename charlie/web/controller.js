$(document).ready(function() {
    // Expose the DisplayMassage function globally
    window.DisplayMassage = function(message) {
        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    };

    window.Showhood = function() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    };
});