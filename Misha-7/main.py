import tkinter as tk
from tkinter import scrolledtext
from itertools import combinations
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

# Функция для обработки нажатия кнопки
def on_generate():
    restrictions = {}
    for day in ['Понедельник', 'Пятница']:
        restriction = restriction_entry.get().strip()
        if restriction:
            restrictions[day] = restriction.split(',')

    plan = generate_plan(restrictions)
    output_text.delete(1.0, tk.END)  # Очистка текстового поля
    output_text.insert(tk.END, "План поедания мороженого на неделю:\n")
    for day, combo in plan.items():
        output_text.insert(tk.END, f"{day}: {combo if combo else 'Нет мороженого'}\n")


root = tk.Tk()
root.title("План поедания мороженого")
root.geometry('%dx%d+%d+%d' % (900, 900, 470, 70))

restriction_label = tk.Label(root, text="Введите ограничения (через запятую)\n(в Понедельник и Пятницу ребёнок не может есть следующие брикеты соответственно):")
restriction_label.pack()

restriction_entry = tk.Entry(root, width=50)
restriction_entry.pack()

available_ice_creams_label = tk.Label(root, text="Доступные брикеты мороженого:")
available_ice_creams_label.pack()

available_ice_creams_text = tk.Text(root, height=5, width=60)
available_ice_creams_text.pack()
available_ice_creams_text.insert(tk.END, "\n".join(ice_creams_with_ingredients.keys()))
available_ice_creams_text.config(state=tk.DISABLED)

generate_button = tk.Button(root, text="Сгенерировать план", command=on_generate)
generate_button.pack()


output_text = scrolledtext.ScrolledText(root, width=60, height=20)
output_text.pack()

root.mainloop()
