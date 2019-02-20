$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".input_fields_wrap"); //Fields wrapper
    var add_button = $(".add_field_button"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append(
                '<div class="row">' +
                '<div class="offset-2 col-sm-6">' +
                '<input type="text" class="form-control" id="ingredients">' +
                '</div>' +
                '<div class="col-sm-2">' +
                '<button class="btn edit_recipe_btn remove_field"><i class="material-icons">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>');
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove field
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        x--;
    })
});
