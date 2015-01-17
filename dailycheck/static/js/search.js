$(document).ready(function() {
    $('#test').keyup(function() {
        var query;
        query = $(this).val();
        $.get('/profile/employlist/', {username: query}, function(data){
            $('#cats').html(data);

        });
    });
});