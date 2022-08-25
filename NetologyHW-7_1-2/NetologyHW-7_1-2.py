from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    shopping_dict = {}
    temp_dict = {}
    counter = 0

    for dish in dishes:
        for ingredients in cook_book:
            if dish == ingredients:
                temp_dict.setdefault(dish, cook_book[ingredients])

    for ingredients in temp_dict.values():
        for el in ingredients:
            if el['ingredient_name'] not in shopping_dict.keys():
                shopping_dict.setdefault(el['ingredient_name'], {'quantity': int(el['quantity']) * person_count, 'measure': el['measure']})
            else:
                shopping_dict[el['ingredient_name']]['quantity'] += int(el['quantity']) * person_count            

    return shopping_dict

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    
    for line in file:
        name = line.replace('\n', '')
        ammount_of_ingredients = int(file.readline())
        recipe = []
        for i in range(ammount_of_ingredients):
            temp = file.readline().replace('\n', '').split(' | ')
            recipe.append({'ingredient_name': temp[0], 
                            'quantity': temp[1], 
                            'measure': temp[2]})
        cook_book.setdefault(name, recipe)
        file.readline()

    pprint(cook_book)
    print()
    pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

    file.close()