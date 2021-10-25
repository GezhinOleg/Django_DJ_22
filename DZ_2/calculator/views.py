from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def is_int(inputstr):
    if inputstr is None:
        return False
    try:
        return int(inputstr)
    except ValueError:
        return False

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe_view(request, dish):
    servings = request.GET.get('servings')
    servings = is_int(servings) if is_int(servings) else 1
    recipe = DATA.get(dish)
    if recipe:
        context = {
            'recipe': {key: value * servings for key, value in recipe.items()}
        }
    else:
        context = {
            'recipe': {dish: 'Нет такого рецепта'}
        }
    return render(request, 'calculator/index.html', context)