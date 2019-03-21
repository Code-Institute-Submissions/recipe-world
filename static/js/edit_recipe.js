//Thank you for Saran for this amazing script
//You can find her explanation here:
//https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(document).ready(function() {
    var max_ingredients_fields = 15;
    var max_methods_fields = 10;
    var ing_fields_wrap = $(".ing_fields_wrap");
    var met_fields_wrap = $(".met_fields_wrap");
    /*var ings1 = $("input[name='ingredients1']").length;*/
    var meths1 = $("input[name='methods1']").length;
    var x;
    var y = meths1;

    inpCounter("ingredients1", "ingredients2");

    function inpCounter(searched) {
        var elem1 = $("input[name='ingredients1']").length;
        var elem2 = $("input[name='ingredients2']").length;
        if (elem1 > 0 && elem2 == 0) {
            x = elem1;
        }
        else if (elem1 == 0 && elem2 > 0) {
            x = elem2;
        }
        else if (elem1 != 0 && elem2 != 0){
            x = elem1 + elem2;
        }
        console.log(elem1, elem2 + " = " + x);
    }
    /*-----------------INGREDIENTS------------------------------*/

    $(".container").on("click", ".add_ing_btn", function() {
        if (x < max_ingredients_fields) {
            x++;
            $(ing_fields_wrap).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<input type="text" class="form-control" name="ingredients2" required>' +
                '</div>' +
                '<div class="col-2">' +
                '<button type="button" class="btn edit_recipe_btn remove_recipe_btn"><i class="material-icons new_line">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>' +
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<button type="button" class="btn edit_recipe_btn add_ing_btn"><i class="material-icons new_line">local_hospital</i></button>' +
                '</div>' +
                '</div>');
            $(this).remove();
        }
        if (x == max_ingredients_fields) {
            $(".add_ing_btn").hide();
        }
        inpCounter();
    });
    
    $("div").on("click", ".remove_recipe_btn", function(e) {
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        x--;
        if (x <= max_ingredients_fields) {
            $(".add_ing_btn").show();
        }
        inpCounter();
        if (x == 1){
            $(this).closest(".remove_recipe_btn").hide();
        }
    })

    /*-----------------METHODS------------------------------*/

    $(".container").on("click", ".add_met_btn", function() {
        if (y < max_methods_fields) {
            y++;
            $(met_fields_wrap).append(
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<textarea class="form-control" name="method2" required></textarea>' +
                '</div>' +
                '<div class="col-2">' +
                '<button type="button" class="btn edit_recipe_btn remove_recipe_btn"><i class="material-icons new_line">do_not_disturb_on</i></button>' +
                '</div>' +
                '</div>' +
                '<div class="row">' +
                '<div class="col-10 offset-md-4 col-md-6">' +
                '<button type="button" class="btn edit_recipe_btn add_met_btn"><i class="material-icons new_line">local_hospital</i></button>' +
                '</div>' +
                '</div>');
            $(this).remove();
        }
        if (y == max_methods_fields) {
            $(".add_met_btn").hide();
        }
    });

    $("div").on("click", ".remove_recipe_btn", function(e) {
        e.preventDefault();
        $(this).parent('div').parent('div').remove();
        y--;
        if (y <= max_methods_fields) {
            $(".add_met_btn").show();
        }
    })
});
