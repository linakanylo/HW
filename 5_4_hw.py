def is_simple(num):
    for i in range (2, round(num/2)):
        if not num % i:
            return False
    return True

numbers = list(range(51))

simple_numbers = list(filter(is_simple, numbers))

squared_numbers = list(map(lambda x: x**2, simple_numbers))

print("Прості числа:", simple_numbers)
print("Квадрати простих чисел:", squared_numbers)

