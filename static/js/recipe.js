//Thank you for Saran for this amazing script
//You can find her explanation here:
//https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(document).ready(function() {
    var max_ingredients_fields = 15;
    var max_method_fields = 10;
    var ingredients_wrapper = $(".ingredients_input_fields_wrap");
    var add_ingredients_button = $(".add_ingredients_field_button");

    var method_wrapper = $(".method_input_fields_wrap");
    var add_method_button = $(".add_method_field_button");

    var x = 1;
    var y = 1;
    $(add_ingredients_button).click(function(e) {
        e.preventDefault();
        if (x < max_ingredients_fields) {
            x++;
            $(ingredients_wrapper).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<input type="text" class="form-control" name="ingredients2" required>' +
                '</div>' +
                '<div class="col-2">' +
                '<button type="button" class="btn edit_recipe_btn remove_field"><i class="material-icons new_line">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>');
        }
        if (x == max_ingredients_fields) {
            $(add_ingredients_button).hide();
        }
    });

    $(ingredients_wrapper).on("click", ".remove_field", function(e) {
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        x--;
        if (x <= max_ingredients_fields) {
            $(add_ingredients_button).show();
        }
    });

    $(add_method_button).click(function(e) {
        e.preventDefault();
        if (y < max_method_fields) {
            y++;
            $(method_wrapper).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<textarea class="form-control" name="method2" required></textarea>' +
                '</div>' +
                '<div class="col-2">' +
                '<button type="button" class="btn edit_recipe_btn remove_field"><i class="material-icons new_line">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>');
        }
        if (y == max_method_fields) {
            $(add_method_button).hide();
        }
    });

    $(method_wrapper).on("click", ".remove_field", function(e) {
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        y--;
        if (x <= max_ingredients_fields) {
            $(add_method_button).show();
        }
    });
});
