$(function (ready) {
    $(document).ready(function () {
        // Detect when a user clicks out of an input box
        $("#ID_OF_INPUT_FIELD").focus(function () {
            // Do nothing
        }).blur(function () {
            document.getElementById("test2").value = document.getElementById("test1").value
        });
        // Repeat this structure as many times as necessary
    });
});
