"""FitLife - приложение для учёта физической активности."""

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)

water_intake = (weight * 30) / 1000

print(f"{name}, ваш индекс массы тела: {bmi}")
print(f"{name}, рекомендуемая норма воды для вас (л/день): {water_intake}.")




