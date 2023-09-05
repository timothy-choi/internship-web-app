$(document).ready(function() {
    $("#cb").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#list tr").filter(function() {
            $(this).toggle($(this).text()
                .toLowerCase().indexOf(value) > -1)
        });
    });
});