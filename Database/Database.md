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

Explanation of the fields:

    | Field name   |                   Explanation of the field                 |
    |--------------|------------------------------------------------------------|
    | cuisine_name | This field contains name of the cuisine                    |
    | pic_url      | This field contains the url for the picture of cuisine     |
    | foods        | This field contains the IDs of all the food in the cuisine |
    |--------------|------------------------------------------------------------|

There are a few relation between them what I write down below.

    "cuisines/foods" <-----------> "foods/id"           - to know which food is in the given cuisine type by ID.
    "mealtypes/mealtype_name" <--> "foods/mealtype_name"- to know which food is in the given meal type by the name of mealtype.
    "foods/favorites" <----------> "users/username"     - to know which food is in the favorites of the users by username.
    "users/my_recipes" <---------> "foods/id"           - to know which food was uploaded by the given user by ID.