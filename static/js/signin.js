$(document).ready(function () {
    $("#signinForm").submit(function (e) {
        e.preventDefault();  // Предотвратить отправку формы
        var formData = $(this).serialize();
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();  // Получить CSRF токен из формы
        formData += '&csrfmiddlewaretoken=' + csrfToken;  // Добавить CSRF токен к данным
        $.ajax({
            type: "POST",
            url: "/login/",
            data: formData,
            success: function (data) {
                if (data.status === 'success') {
                    $('#singInModal').modal('hide');// Закрыть модальное окно
                    location.reload(); // Обновить страницу
                }
            },
        });
    });
});