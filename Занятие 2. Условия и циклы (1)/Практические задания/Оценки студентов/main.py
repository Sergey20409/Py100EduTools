# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]
for st in students:
    if st['grade'] > 3:
        print(st['name'],". Оценка: ", st['grade'],sep='')

# TODO Распечатать имена студентов с оценками выше тройки
