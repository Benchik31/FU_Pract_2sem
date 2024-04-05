$(document).ready(function () {
    $("#signupForm").submit(function (e) {
        e.preventDefault();
        var formData = $(this).serialize();
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        formData += '&csrfmiddlewaretoken=' + csrfToken;

        $.ajax({
            type: "POST",
            url: "/signup/",
            data: formData,
            dataType: 'json',  // Указываем, что ожидаем JSON в ответе
            success: function (data) {
                if (data.status === 'success') {
                    $('#singUpModal').modal('hide');
                    location.reload();
                }
            },
        });
    });
});