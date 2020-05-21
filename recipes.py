from context_manager import open_time_log


def recipe_rewrite(output_name, input_name):
    with open_time_log(output_name, input_name) as recipes:
        cook_book = {}
        def recipe_rewrite():
            dish = recipes.readline().strip()
            if dish:
                cook_book[dish] = []
                ingredient_number = recipes.readline()
                for line in range(int(ingredient_number)):
                    ingredient = recipes.readline().strip().split(' | ')
                    ingredient_dictionary = {'ingredient name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                    cook_book[dish].append(ingredient_dictionary)
            else:
                return(cook_book)
            recipes.readline()
            recipe_rewrite()
        recipe_rewrite()
    return(cook_book)

print(recipe_rewrite('recipes.txt', 'recipes_logs.txt'))
