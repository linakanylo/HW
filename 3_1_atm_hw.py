def atm_withdraw(amount, available_notes):
    # Сортуємо доступні купюри у спадаючому порядку
    sorted_notes = sorted(available_notes, reverse=True)

    # Створюємо словник, де ключ - це номінал купюри, а значення - кількість купюр цього номіналу
    notes_count = {note: 0 for note in sorted_notes}

    # Ініціалізуємо зміну для суми, яку ще потрібно видачі
    remaining_amount = amount

    # Проходимо по номіналах купюр та видаємо їх, якщо можна
    for note in sorted_notes:
        if remaining_amount >= note and available_notes[note] > 0:
            # Знаходимо кількість купюр цього номіналу, які можна видасти
            num_notes = min(remaining_amount // note, available_notes[note])

            # Віднімаємо видачу від залишку грошей
            remaining_amount -= num_notes * note

            # Оновлюємо кількість купюр цього номіналу, які залишилися
            notes_count[note] = num_notes

    # Перевіряємо, чи було можливо видасти вказану суму
    if remaining_amount == 0:
        print("Видача грошей:")
        for note, count in notes_count.items():
            if count > 0:
                print(f"{note} грн x {count}")
    else:
        print("Неможливо видасти вказану суму")

# Приклад використання функції
available_notes = {1000: 5, 500: 10, 200: 20, 100: 50}
withdraw_amount = 2800
atm_withdraw(withdraw_amount, available_notes)
