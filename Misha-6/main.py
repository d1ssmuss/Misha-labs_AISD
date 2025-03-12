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


def function_python():
    # Подход с помощью функций Питона
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


    # Ограничение: не более 2 сладких брикетов
    def is_valid_combination(combo):
        sweet_count = sum(1 for ice_cream in combo if 'сладкий' in ice_creams_with_ingredients[ice_cream])
        return sweet_count <= 2


    # Генерация всех допустимых комбинаций
    valid_combinations = []
    # 0 брикетов
    valid_combinations.append(())
    # 1 брикет
    valid_combinations.extend([(ice_cream,) for ice_cream in ice_creams_with_ingredients.keys()])
    # 2 брикета
    valid_combinations.extend(
        [combo for combo in combinations(ice_creams_with_ingredients.keys(), 2) if is_valid_combination(combo)]
    )


    # Генерация вариантов поедания мороженого на неделю без повторного использования брикетов
    def generate_weekly_plan(valid_combinations):
        weekly_plan = {}
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        # Список для хранения использованных брикетов
        used_ice_creams = set()

        for day in days_of_week:
            # Фильтруем допустимые комбинации, чтобы исключить уже использованные брикеты
            available_combinations = [combo for combo in valid_combinations if
                                      not any(ice_cream in used_ice_creams for ice_cream in combo)]

            if available_combinations:
                chosen_combo = random.choice(available_combinations)
                weekly_plan[day] = chosen_combo

                # Добавляем выбранные брикеты в список использованных
                used_ice_creams.update(chosen_combo)
            else:
                weekly_plan[day] = "Нет доступных брикетов"

        return weekly_plan


    # Создаем план на неделю
    weekly_plan = generate_weekly_plan(valid_combinations)

    # Выводим план
    print("План поедания мороженого на неделю:")
    for day, combo in weekly_plan.items():
        print(f"{day}: {combo if combo else 'Нет мороженого'}")


# Алгоритмический подход


def algoritmich():
    # Список брикетов мороженого
    ice_creams = ['Ваниль', 'Шоколад', 'Клубника', 'Мята', 'Карамель', 'Кофе', 'Фисташка', 'Лимон', 'Кокос', 'Черника']

    # Список для хранения всех допустимых комбинаций
    valid_combinations = []

    # Генерация ВСЕХ допустимых комбинаций (0, 1 и 2 брикета)
    # 0 брикетов
    valid_combinations.append(())

    # 1 брикет
    for i in range(len(ice_creams)):
        valid_combinations.append((ice_creams[i],))

    # 2 брикета
    for i in range(len(ice_creams)):
        for j in range(i + 1, len(ice_creams)):
            valid_combinations.append((ice_creams[i], ice_creams[j]))

    # Генерация плана на неделю
    weekly_plan = {}
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    # Список для хранения использованных брикетов
    used_ice_creams = []

    # print(valid_combinations)
    for day in days_of_week:
        # Фильтруем доступные комбинации
        available_combinations = []
        for combo in valid_combinations:
            if all(ice_cream not in used_ice_creams for ice_cream in combo):
                available_combinations.append(combo)

        # print(f"*"*15, available_combinations)

        if available_combinations:
            # Выбираем случайную комбинацию
            chosen_combo = random.choice(available_combinations)
            # print("chosen_combo", chosen_combo)
            weekly_plan[day] = chosen_combo

            # Добавляем выбранные брикеты в список использованных
            for ice_cream in chosen_combo:
                used_ice_creams.append(ice_cream)
        else:
            weekly_plan[day] = "Нет доступных брикетов"

    # Выводим план
    print("План поедания мороженого на неделю:")
    for day in days_of_week:
        combo = weekly_plan[day]
        if combo:
            print(f"{day}: {combo if combo else 'Нет мороженого'}")
        else:
            print(f"{day}: Нет мороженого")

print("Алгоритмический подход:")
print()
algoritmich()
print()
print("Подход с помощью функций Питона:")
print()
function_python()