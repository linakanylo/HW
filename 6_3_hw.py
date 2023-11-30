from collections import Counter

with open(r'C:\Users\Lenovo\Desktop\richard.txt', 'r') as file:
    words = file.read().split()

word_counts = Counter(words)

with open(r'C:\Users\Lenovo\Desktop\richard1.txt', 'w') as output_file:
    for word, count in word_counts.items():
        output_file.write(f'{word}: {count}\n')



