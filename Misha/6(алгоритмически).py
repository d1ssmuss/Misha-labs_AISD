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
def is_valid_combination(combo, used_ice_creams):
    sweet_count = sum(1 for ice_cream in combo if 'сладкий' in ice_creams_with_ingredients[ice_cream])
    if sweet_count > 2:
        return False
    return True


# Функция для генерации всех возможных комбинаций брикетов
def generate_combinations(ice_creams):
    combinations = []
    n = len(ice_creams)

    # Генерация одиночных брикетов
    for i in range(n):
        combinations.append((ice_creams[i],))

    # Генерация пар брикетов
    for i in range(n):
        for j in range(i + 1, n):
            combinations.append((ice_creams[i], ice_creams[j]))

    return combinations


# Функция для генерации плана поедания мороженого
def generate_plan():
    ice_creams = list(ice_creams_with_ingredients.keys())
    valid_combinations = [()] + generate_combinations(ice_creams)

    weekly_plan = {}
    used_ice_creams = []

    # Генерация случайного плана на неделю
    for day in range(7):  # 7 дней в неделе
        available_combinations = [
            combo for combo in valid_combinations
            if is_valid_combination(combo, used_ice_creams) and
               not any(ice_cream in used_ice_creams for ice_cream in combo)
        ]

        if available_combinations:
            chosen_combo = random.choice(available_combinations)
            weekly_plan[f"День {day + 1}"] = chosen_combo
            used_ice_creams.extend(chosen_combo)
        else:
            weekly_plan[f"День {day + 1}"] = "Нет доступных брикетов"

    return weekly_plan


def main():
    print("Доступные брикеты мороженого:")
    for ice_cream in ice_creams_with_ingredients.keys():
        print(f"- {ice_cream}")

    # Генерация плана
    plan = generate_plan()

    print("\nПлан поедания мороженого на неделю:")
    for day, combo in plan.items():
        print(f"{day}: {combo if combo else 'Нет мороженого'}")


if __name__ == "__main__":
    main()