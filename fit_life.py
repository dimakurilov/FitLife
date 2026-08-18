# -*- coding: utf-8 -*-
"""FitLife - приложение для учёта физической активности."""

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Недостаточный вес"
elif 18.5 <= bmi < 25:
    category = "Нормальный вес"
elif 25 <= bmi < 30:
    category = "Избыточный вес"
else:
    category = "Ожирение"

print(f"{name}, ваш индекс массы тела: {bmi:.2f}")
print(f"Категория: {category}")
