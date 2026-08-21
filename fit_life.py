"""FitLife - приложение для учёта физической активности."""

# Константы для расчётов
WATER_PER_KG_ML = 30  # мл воды на 1 кг веса
ML_PER_LITER = 1000   # количество миллилитров в литре

user_name = input("Введите ваше имя: ").strip()
while not user_name:
    user_name = input("Имя не может быть пустым! Введите имя: ").strip()
age = int(input("Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес (кг): "))
user_height = float(input("Введите ваш рост (м): "))

bmi = round(user_weight / (user_height ** 2), 1)

water_intake = (user_weight * WATER_PER_KG_ML) / ML_PER_LITER

print(f"Ваш индекс массы тела: {bmi}")
print(
    f"{user_name}, рекомендуемая норма воды для вас (л/день): "
    f"{water_intake}.",
)
