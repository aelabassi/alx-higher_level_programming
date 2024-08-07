$(() => {
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        type: "GET",
        success: (data) => {
            $("#hello").text(data.hello);
        }
    })
})
