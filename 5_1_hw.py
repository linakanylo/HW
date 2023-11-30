#створюємо словник оцінок студентів
student_grades = {
    'Польова Іванна': [90, 79, 56, 89, 99],
    'Іванченко Дмитро': [99, 78, 67, 56, 89],
    'Скорик Владислава': [56, 78, 78, 99, 90],
    'Міхно Валерій': [45, 99, 99, 89, 56],
    'Бограч Катерина': [67, 78, 56, 45, 99],
    'Борщ Роман': [56, 78, 99, 89, 90]
}

#функція для знаходження середнього балу студентів
def calculate_average(grades):
    return sum(grades) / len(grades)

# Знаходимо найуспішнішого і найслабкішого студента
best_student = None
worst_student = None
best_average = float('-inf')
worst_average = float('inf')

for student, grades in student_grades.items():
    average = calculate_average(grades)
    if average > best_average:
        best_student = student
        best_average = average
    if average < worst_average:
        worst_student = student
        worst_average = average

print(f"Найуспішніший студент: {best_student} (Середній бал: {best_average})")
print(f"Найслабкіший студент: {worst_student} (Середній бал: {worst_average})")




