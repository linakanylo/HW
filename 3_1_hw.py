with open('input.txt', 'r') as f:
    for line in f:

        numbers = [int(num) for num in line.split()]

        for num in numbers:
            output = ""
            if num % 2 == 0 and num % 3 == 0:
                output += "FizzBuzz"
            elif num % 2 == 0:
                output += "Fizz"
            elif num % 3 == 0:
                output += "Buzz"
            else:
                output = num

            print(output, end=' ')
        print()

