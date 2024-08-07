
$(document).ready(() => {
    $(() => {
        $("INPUT#btn_translate").click(() => {
            const lang = $("INPUT#language_code").val();
            $.ajax({
                url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
                type: "GET",
                success: (data) => {
                    $("#hello").text(data.hello);
                }
            });
        });
        $("INPUT#language_code").keypress((e) => {
            if (e.which === 13) {
                $("INPUT#btn_translate").click();
            }
        });
    });
});
