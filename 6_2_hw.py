def squaring_number(num):
    return num ** 2

def is_simple(num):
    if num < 2:
        return False
    for i in range(2, round(num/2)):
        if num % i == 0:
            return False
    return True

numbers = list(range(51))  # Створимо список чисел від 0 до 50

is_simple = list(filter(is_simple, numbers))  # Відфільтруємо прості числа

squaring_number = list(map(squaring_number, is_simple))  # Піднесемо прості числа у квадрат

print("Квадрати простих чисел в діапазоні від 0 до 50:")
for num, square in zip(is_simple, squaring_number):
    print(f"{num} ^ 2 = {square}")

