# Функція для перетворення рядка до нижнього регістру
def to_lower_case(s):
    return s.lower()

# Функція для перетворення рядка до верхнього регістру
def to_upper_case(s):
    return s.upper()

# Головна програма
if __name__ == "__main__":
    # Список рядків
    strings = ["Hello, World!", "This is a Sample String", "Python Programming"]

    # Використовуємо функцію map для перетворення кожного рядка до нижнього регістру
    lower_case_strings = list(map(to_lower_case, strings))

    # Використовуємо функцію map для перетворення кожного рядка до верхнього регістру
    upper_case_strings = list(map(to_upper_case, strings))

    # Виводимо результати
    print("Рядки в нижньому регістрі:")
    for s in lower_case_strings:
        print(s)

    print("\nРядки в верхньому регістрі:")
    for s in upper_case_strings:
        print(s)
