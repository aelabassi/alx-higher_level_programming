$(() => {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        type: "GET",
        success: (data) => {
            data.results.forEach((film) => {
                $("#list_movies").append($("<li></li>").text(film.title));
            });
        }
    })
})
