print('Привет!', "Я виртуальный помощник от Fitlife!")
print('Мне потребуются твои данные для расчета ИМТ.')
user_name = input('Как я могу к тебе обращаться?')
print(user_name.title(), 'рад знакомству!')

user_age = int(input('Введи свой возраст : '))
user_weight = float(input('Введи свой вес в кг : '))
user_height = float(input('Введи свой рост в м (пример - 1.55): '))

"""Расчет ИМТ"""
bmi = round(user_weight / (user_height ** 2), 1)


water_intake = (user_weight * 30) / 1000

print(f"Ваш индекс массы тела: {bmi}")
print(
    f"{user_name}, рекомендуемая норма воды для вас (л/день): "
    f"{water_intake}.",
)
