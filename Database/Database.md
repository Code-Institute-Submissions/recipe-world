I used a non relational database, named MongoDB to store data.
You can see how the collections look like:

    | Cuisines     | Meal Types    | Foods         | Users      |
    |--------------|---------------|---------------|------------|
    | cuisine_name | mealtype_name | cuisine_name  | username   |
    | pic_url      |               | mealtype_name | email      |
    | foods        |               | name          | my_recipes |
    |              |               | author        | favorites  |
    |              |               | uploaded_by   |            |
    |              |               | description   |            |
    |              |               | pic_url       |            |
    |              |               | ingredients   |            |
    |              |               | method        |            |
    |              |               | favorites     |            |
    |--------------|---------------|---------------|------------|

Explanation of the fields of Cuisines:

    | Field name   |                   Explanation of the field                 |
    |--------------|------------------------------------------------------------|
    | cuisine_name | This field contains name of the cuisine                    |
    | pic_url      | This field contains the url for the picture of cuisine     |
    | foods        | This field contains the IDs of all the food in the cuisine |
    |--------------|------------------------------------------------------------|

Explanation of the fields of Meal Types:

    | Field name    |         Explanation of the field          |
    |---------------|-------------------------------------------|
    | mealtype_name | This field contains the name of mealtypes |
    |---------------|-------------------------------------------|
    
Explanation of the fields of Foods:

    |  Field name   | Explanation of the field                                     |
    |---------------|--------------------------------------------------------------|
    | cuisine_name  | This field contains the name of the cuisine type of the food |
    | mealtype_name | This field contains the name of the meal type of the food    |
    | name          | This field contains the name of the food                     |
    | author        | This field contains the name of the author of the food       |
    | uploaded_by   | This field contains the name of the uploader of the food     |
    | description   | This field contains the short description of the food        |
    | pic_url       | This field contains the url for the picture of the food      |
    | ingredients   | This field contains the ingredients of the food              |
    | method        | This field contains the method of how to make the food       |
    | favorites     | This field contains the IDs of users how like the food       |
    |---------------|--------------------------------------------------------------|

Explanation of the fields of Users:   

    |  Field name | Explanation of the field                                  |
    |-------------|-----------------------------------------------------------|
    | username    | This field contains the username of the user              |
    | email       | This field contains the email address of the user         |
    | my_recipes  | This field contains the IDs of recipes what user uploaded |
    | favorites   | This field contains the IDs of recipes what user likes    |
    |-------------|-----------------------------------------------------------|

There are a few relation between them what I write down below.

    "cuisines/foods" <-----------> "foods/id"           - to know which food is in the given cuisine type by ID.
    "mealtypes/mealtype_name" <--> "foods/mealtype_name"- to know which food is in the given meal type by the name of mealtype.
    "foods/favorites" <----------> "users/username"     - to know which food is in the favorites of the users by username.
    "users/my_recipes" <---------> "foods/id"           - to know which food was uploaded by the given user by ID.