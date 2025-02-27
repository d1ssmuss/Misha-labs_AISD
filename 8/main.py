"""
Айдашкин Михаил ИСТбд-23
ЛР №8
Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом.
Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных не использовать.
При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами. Для GUI использовать библиотеку tkinter.

Вариант 2  Объекты – треугольники
Функции:	проверка пересечения
визуализация
раскраска
перемещение на плоскости
"""
from tkinter.messagebox import showerror, showwarning, showinfo
import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
import math

class Triangle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.triangles = [] # треугольники
        self.current_triangle = None
        # Привязываем события для каждого треугольника
        for tringl in self.triangles:
            self.canvas.tag_bind(tringl, "<ButtonPress-1>", self.on_button_press)
            self.canvas.tag_bind(tringl, "<B1-Motion>", self.on_mouse_drag)
        self.offset_x = 0
        self.offset_y = 0
        self.center_x = 0
        self.center_y = 0

    def on_button_press(self, event):
        self.current_triangle = self.canvas.find_closest(event.x, event.y)[0]
        x, y = self.canvas.coords(self.current_triangle)[:2]
        self.offset_x = event.x - x
        self.offset_y = event.y - y

    def on_mouse_drag(self, event):
        if self.current_triangle:
            self.canvas.move(self.current_triangle, event.x - self.offset_x - self.canvas.coords(self.current_triangle)[0],
                             event.y - self.offset_y - self.canvas.coords(self.current_triangle)[1])

    def open_file(self): # открытие файла
        # Открываем диалог для выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    # Разбиваем строку на части
                    parts = line.strip().split(', ')
                    # print(parts)
                    x0, y0, x1, y1, x2, y2 = map(int, parts[:6])
                    fill = parts[6]
                    outline = parts[7]
                    width = int(parts[8])

                    # Создаем дугу на основе данных из файла
                    triangle = self.canvas.create_polygon((x0, y0), (x1, y1), (x2,y2), fill=fill, outline=outline, width=width)
                    self.triangles.append(triangle)

                    # Привязываем события для новой дуги
                    self.canvas.tag_bind(triangle, "<ButtonPress-1>", self.on_button_press)
                    self.canvas.tag_bind(triangle, "<B1-Motion>", self.on_mouse_drag)

    def change_color(self):
        if self.current_triangle:
            color = colorchooser.askcolor()[1]  # Получаем выбранный цвет
            if color:
                self.canvas.itemconfig(self.current_triangle, fill=color)  # Меняем цвет сектора

    def show_information_about_program(self):
        window = tk.Tk()
        window.title("Информация")
        window.geometry('%dx%d+%d+%d' % (1400, 400, 250, 250))
        label = tk.Label(window, text="**О программе**\n"
                                      "В данной программе, пользователь работает с треугольниками. Примечание:\n"
                                      "1. Файл должен иметь расширение .txt (имя файла любое) и находиться в директории проекта.\n"
                                      "2. Txt-файл содержит информацию о треугольниках, где каждая строка описывает один треугольник.\n"
                                      "3. Каждая строка состоит из 8 объектов, разделенных запятыми:\n"
                                      "   - Первые шесть чисел, которые задают треугольник: x0, y0, x1, y1, x2, y2\n"
                                      "   - Далее идут цвет заполнения фигуры, цвет контура фигуры и ширина\n"
                                      "4. Для того чтобы проверить пересечение, можно нажать на кнопку 'Найти пересечение'\n"
                                      "5. Чтобы изменить цвет треугольника нужно выбрать треугольник(с помощью ЛКМ) и нажать на 'Изменить цвет'\n",
                         font=("Times New Roman", 21))
        label.pack()

    def find_first_intersection(self):
        for x in range(0, 600):
            for y in range(0, 600):
                if self.check_intersection(x, y):
                    return (x, y)
        return None

    def check_intersection(self, x, y):
        overlapping_arcs = self.canvas.find_overlapping(x, y, x, y)
        return len(overlapping_arcs) >= 2

    def show_intersection(self):
        intersection_point = self.find_first_intersection()
        if intersection_point:
            x, y = intersection_point
            tk.messagebox.showinfo("Пересечение", "Пересечение найдено!")
        else:
            tk.messagebox.showinfo("Пересечение", "Пересечений не найдено.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('%dx%d+%d+%d' % (1366, 860, 270, 85))
    root.title('Треугольники')
    canvas = tk.Canvas(root, width=1320, height=550, bg='white', highlightbackground="green")
    canvas.place(x=20, y=0)
    Trngle = Triangle(canvas)
    # Кнопки
    button_open_file = tk.Button(root, text="Открыть файл", command=Trngle.open_file, font=("Arial", 22),bg="lightblue")
    button_open_file.place(x=40, y=600, width=290)
    # Добавляем кнопку для поиска пересечений
    button = tk.Button(root, text="Найти пересечение", command=Trngle.show_intersection, font=("Arial", 22), bg="lightblue")
    button.place(x=350, y=600)
    # Добавляем кнопку для изменения цвета
    button_color = tk.Button(root, text="Изменить цвет", command=Trngle.change_color, font=("Arial", 22), bg="lightblue")
    button_color.place(x=660, y=600, width=290)
    button_info = tk.Button(root, text="Информация", command=Trngle.show_information_about_program,
                            font=("Arial", 22), bg="lightblue")
    button_info.place(x=980, y=600, width=290)
    root.mainloop()