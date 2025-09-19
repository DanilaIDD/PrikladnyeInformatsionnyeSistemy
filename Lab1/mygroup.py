groupmates = [
    {
        "name": "Марат",
        "surname": "Дреев",
        "exams": ["АиГ", "Философия", "ВВиТ"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Алиса",
        "surname": "Завьялова",
        "exams": ["ВМ", "История", "ВТ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Данила",
        "surname": "Иванов",
        "exams": ["ППСУБДиЗ", "АИС", "РОС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Михаил",
        "surname": "Ильин",
        "exams": ["ТВиМС", "Физика", "ИТиП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Денис",
        "surname": "Истомин",
        "exams": ["КТП", "Английский язык", "СиАОД"],
        "marks": [3, 3, 5]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

def print_students_sort(students, n):
    # Фильтрация студентов
    filtered_students = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > n:
            filtered_students.append(student)
    if filtered_students:
        print(f"\nСтуденты со средним баллом выше {n}:")
        print_students(filtered_students)
    else:
        print(f"\nНет студентов со средним баллом выше {n}")

n = float(input("Введите целевой средний балл: "))
print_students_sort(groupmates, n)
