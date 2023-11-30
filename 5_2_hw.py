# Структура даних для студентів
students = [
    {"імя": "Іван", "прізвище": "Петров", "групи": ["Python", "FullStack"]},
    {"імя": "Марія", "прізвище": "Іванова", "групи": ["FrontEnd"]},
    {"імя": "Петро", "прізвище": "Сидоров", "групи": ["Python", "Java"]},
    {"імя": "Олена", "прізвище": "Коваленко", "групи": ["FrontEnd", "Java"]},
    {"імя": "Анна", "прізвище": "Морозова", "групи": ["Python", "FrontEnd"]},
]

# Знайти студентів, які навчаються у двох та більше групах
students_in_multiple_groups = [student for student in students if len(student["групи"]) >= 2]

# Знайти студентів, які не навчаються на фронтенді
students_not_in_FrontEnd = [student for student in students if "FrontEnd" not in student["групи"]]

# Знайти студентів, які вивчають Python або Java
students_python_or_java = [student for student in students if "Python" in student["групи"] or "Java" in student["групи"]]

# Друк для відлагодження
print("Студенти, які навчаються у двох та більше групах:")
for student in students_in_multiple_groups:
    print(f"{student['імя']} {student['прізвище']} навчається у групах: {', '.join(student['групи'])}")

print("\nСтуденти, які не навчаються на фронтенді:")
for student in students_not_in_FrontEnd:
    print(f"{student['імя']} {student['прізвище']} не навчається на фронтенді")

print("\nСтуденти, які вивчають Python або Java:")
for student in students_python_or_java:
    print(f"{student['імя']} {student['прізвище']} вивчає {', '.join(group for group in student['групи'] if group in ['Python', 'Java'])}")
