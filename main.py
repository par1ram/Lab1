groupmates = [
    {
        "name": "Владислав",
        "surname": "Хорунжий",
        "exams": ["АиГ", "ВВИТ", "Философия"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Артем",
        "surname": "Бобков",
        "exams": ["АиГ", "ВВИТ", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Вероника",
        "surname": "Парамонова",
        "exams": ["АиГ", "ВВИТ", "Философия"],
        "marks": [4, 3, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Ясинский",
        "exams": ["АиГ", "ВВИТ", "Философия"],
        "marks": [5, 4, 2]
    },
    {
        "name": "Али",
        "surname": "Калбаев",
        "exams": ["АиГ", "ВВИТ", "Философия"],
        "marks": [5, 4, 5]
    }
]

average_mark = float(input("Введите средний балл: "))


def filter_students(students, average_mark):
    filtered_students = []
    for student in students:
        if sum(student["marks"])/len(student["marks"]) > average_mark:
            filtered_students.append(student)
    return filtered_students


filtered_students = filter_students(groupmates, average_mark)
print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
for student in filtered_students:
    print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
    str(student["marks"]).ljust(20))
