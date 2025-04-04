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
        if day in selected_ice_creams:
            restrictions[day] = selected_ice_creams[day]

    plan = generate_plan(restrictions)
    output_text.delete(1.0, tk.END)  # Очистка текстового поля
    output_text.insert(tk.END, "План поедания мороженого на неделю:\n")
    for day, combo in plan.items():
        output_text.insert(tk.END, f"{day}: {combo if combo else 'Нет мороженого'}\n")

def select_day(day):
    if day in selected_days:
        selected_days.remove(day)
        day_buttons[day].config(bg='SystemButtonFace')
    else:
        selected_days.append(day)
        day_buttons[day].config(bg='gray')

def select_ice_cream(ice_cream):
    for day in selected_days:
        if day in selected_ice_creams:
            selected_ice_creams[day].append(ice_cream)
        else:
            selected_ice_creams[day] = [ice_cream]
        day_buttons[day].config(bg='green')
        ice_cream_buttons[ice_cream].config(bg='lightblue')  # Change color of selected ice cream button

root = tk.Tk()
root.title("План поедания мороженого")
root.geometry('%dx%d+%d+%d' % (900, 1000, 470, 0))

selected_days = []
selected_ice_creams = {}

# Создание метки с инструкцией
instruction_label = tk.Label(root, text="Выберите вид мороженого, который ребёнок не может взять:", font=('Arial', 16))
instruction_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')

# Создание кнопок для дней
day_buttons = {}
for i, day in enumerate(['Понедельник', 'Пятница']):
    day_buttons[day] = tk.Button(root, text=day, command=lambda d=day: select_day(d), width=20, height=3, font=('Arial', 14))
    day_buttons[day].grid(row=1, column=i, padx=10, pady=10, sticky='ew')

# Создание кнопок для мороженого
ice_cream_buttons = {}
for i, ice_cream in enumerate(ice_creams_with_ingredients.keys()):
    ice_cream_buttons[ice_cream] = tk.Button(root, text=ice_cream, command=lambda i=ice_cream: select_ice_cream(i), width=10, height=3, font=('Arial', 14))
    row = i // 2 + 2  # Размещаем по две кнопки в строке, начиная с 2-й строки
    col = i % 2
    ice_cream_buttons[ice_cream].grid(row=row, column=col, padx=10, pady=10, sticky='ew')

generate_button = tk.Button(root, text="Сгенерировать план", command=on_generate, width=10, height=2, font=('Arial', 14))
generate_button.grid(row=7, column=0, columnspan=2, pady=20, sticky='ew')

output_text = scrolledtext.ScrolledText(root, width=60, height=10, font=('Arial', 12))
output_text.grid(row=8, column=0, columnspan=2, pady=10, sticky='ew')

# Конфигурация сетки для центрирования
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
