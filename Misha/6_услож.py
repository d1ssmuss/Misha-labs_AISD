"""
Айдашкин Михаил ИСТбд-23
Задание на л.р. №6
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 2. В холодильнике 10 брикетов мороженого разного вида.
Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю.
"""
import random
from itertools import combinations

# Список брикетов мороженого с их характеристиками
ice_creams_with_ingredients = {
    'Ваниль': ['сладкий'],
    'Шоколад': ['сладкий'],
    'Клубника': ['сладкий'],
    'Мята': ['не сладкий'],
    'Карамель': ['сладкий'],
    'Кофе': ['не сладкий'],
    'Фисташка': ['не сладкий'],
    'Лимон': ['не сладкий'],
    'Кокос': ['сладкий'],
    'Черника': ['не сладкий']
}

# Функция для проверки допустимости комбинации
def is_valid_combination(combo, used_ice_creams, day, restrictions):
    sweet_count = sum(1 for ice_cream in combo if 'сладкий' in ice_creams_with_ingredients[ice_cream])
    if sweet_count > 2:
        return False
    if any(ice_cream in restrictions.get(day, []) for ice_cream in combo):
        return False
    return True

# Функция для генерации плана поедания мороженого
def generate_plan(restrictions):
    valid_combinations = [()] + [(ice_cream,) for ice_cream in ice_creams_with_ingredients.keys()]
    valid_combinations += [combo for combo in combinations(ice_creams_with_ingredients.keys(), 2)]

    weekly_plan = {}
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    used_ice_creams = []

    for day in days_of_week:
        available_combinations = [
            combo for combo in valid_combinations
            if is_valid_combination(combo, used_ice_creams, day, restrictions) and
               not any(ice_cream in used_ice_creams for ice_cream in combo)
        ]

        if available_combinations:
            chosen_combo = random.choice(available_combinations)
            weekly_plan[day] = chosen_combo
            used_ice_creams.extend(chosen_combo)
        else:
            weekly_plan[day] = "Нет доступных брикетов"

    return weekly_plan


def main():
    print("Доступные брикеты мороженого:")
    for ice_cream in ice_creams_with_ingredients.keys():
        print(f"- {ice_cream}")

    # Ввод ограничений
    print("Примечание: Ввод мороженного с большой буквы!")
    monday_restriction = input("Введите мороженое, которое нельзя есть в Понедельник: ").capitalize()
    friday_restriction = input("Введите мороженое, которое нельзя есть в Пятницу: ").capitalize()

    restrictions = {}
    if monday_restriction:
        restrictions['Понедельник'] = [ice.strip() for ice in monday_restriction.split(',')]
    if friday_restriction:
        restrictions['Пятница'] = [ice.strip() for ice in friday_restriction.split(',')]

    # Генерация плана
    plan = generate_plan(restrictions)

    print("\nПлан поедания мороженого на неделю:")
    for day, combo in plan.items():
        print(f"{day}: {combo if combo else 'Нет мороженого'}")

if __name__ == "__main__":
    main()