"""FitLife - приложение для учёта физической активности."""

user_name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес (кг): "))
user_height = float(input("Введите ваш рост (м): "))

bmi = round(user_weight / (user_height ** 2), 1)

water_intake = (user_weight * 30) / 1000

print(f"Ваш индекс массы тела: {bmi}")
print(
    f"{user_name}, рекомендуемая норма воды для вас (л/день): "
    f"{water_intake}.",
)
