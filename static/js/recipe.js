$(document).ready(function() {
    var max_ingredients_fields = 15; //maximum input boxes allowed
    var max_method_fields = 10; //maximum input boxes allowed
    var ingredients_wrapper = $(".ingredients_input_fields_wrap"); //Fields wrapper
    var add_ingredients_button = $(".add_ingredients_field_button"); //Add button ID
    
    var method_wrapper = $(".method_input_fields_wrap"); //Fields wrapper
    var add_method_button = $(".add_method_field_button"); //Add button ID

    var x = 1; //initlal text box count
    var y = 1; //initlal text box count
    $(add_ingredients_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_ingredients_fields) { //max input box allowed
            x++; //text box increment
            $(ingredients_wrapper).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<input type="text" class="form-control" name="ingredients2">' +
                '</div>' +
                '<div class="col-1">' +
                '<button class="btn edit_recipe_btn remove_field"><i class="material-icons">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>');
        }
    });

    $(ingredients_wrapper).on("click", ".remove_field", function(e) { //user click on remove field
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        x--;
    })
    
    $(add_method_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (y < max_method_fields) { //max input box allowed
            y++; //text box increment
            $(method_wrapper).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<textarea class="form-control" name="method2"></textarea>' +
                '</div>' +
                '<div class="col-1">' +
                '<button class="btn edit_recipe_btn remove_field"><i class="material-icons">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>');
        }
    });

    $(method_wrapper).on("click", ".remove_field", function(e) { //user click on remove field
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        y--;
    })
});
