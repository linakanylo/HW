with open("C:\\Users\\Lenovo\\Desktop\\input.txt", 'r') as f:
    for line in f:

        numbers = [int(num) for num in line.split()]

        for num in numbers:
            output = ""
            if num % 2 == 0:
                output += "Fizz"
            if num % 3 == 0:
                output += "Buzz"

            if not output:
                output = num

            print(output, end=' ')
        print()
