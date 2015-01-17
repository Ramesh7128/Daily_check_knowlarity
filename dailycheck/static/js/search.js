$(document).ready(function() {
    $('#test').keyup(function() {
        var query;
        query = $(this).val();
        $.get('/profile/employeelist/', {username: query}, function(data){
            $('#cats').html(data);

        });
    });
});