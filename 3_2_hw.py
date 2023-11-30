input_filename = 'C:\\Users\\Lenovo\\Desktop\\input.txt'
output_filename = 'C:\\Users\\Lenovo\\Desktop\\output.txt'

with open('C:\\Users\\Lenovo\\Desktop\\input.txt', 'r') as input_file, open('C:\\Users\\Lenovo\\Desktop\\output.txt', 'w') as output_file:
    for line in input_file:
        numbers = [int(num) for num in line.split()]

        for num in numbers:
            output = ""
            if num % 2 == 0:
                output += "Fizz"
            if num % 3 == 0:
                output += "Buzz"

            if not output:
                output = str(num)

            output_file.write(output + ' ')
        output_file.write('\n')
