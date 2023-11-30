def перекласти_розмір_верхнього_одягу(міжнародний_розмір):

    розміри_переклад = {
        "S": {"Норвегія, Фінляндія, Швеція": 34, "Франція, Швейцарія": 36, "Італія": 38, "Британія": 8, "США": 6},
        "M": {"Норвегія, Фінляндія, Швеція": 36, "Франція, Швейцарія": 38, "Італія": 40, "Британія": 10, "США": 8},
        "L": {"Норвегія, Фінляндія, Швеція": 40, "Франція, Швейцарія": 42, "Італія": 44, "Британія": 14, "США": 12},
        "XL": {"Норвегія, Фінляндія, Швеція": 44, "Франція, Швейцарія": 46, "Італія": 48, "Британія": 18, "США": 16},
        "XXL": {"Норвегія, Фінляндія, Швеція": 48, "Франція, Швейцарія": 50, "Італія": 52, "Британія": 22, "США": 20},
    }

    if міжнародний_розмір in розміри_переклад:
        return розміри_переклад[міжнародний_розмір]
    else:
        return "Розмір не знайдено"

міжнародний_розмір = "S"
результат = перекласти_розмір_верхнього_одягу(міжнародний_розмір)
print(f"Міжнародний розмір верхнього одягу {міжнародний_розмір} відповідає розмірам: 'Норвегія, Фінляндія, Швеція' {результат['Норвегія, Фінляндія, Швеція']}, Франція, Швейцарія {результат['Франція, Швейцарія']}, Італія {результат['Італія']}, Британія {результат['Британія']}, США {результат['США']}")


def перекласти_розмір_жіночої_білизни(міжнародний_розмір):

    розміри_переклад = {
        "XXS": {"Німеччина": 36, "США": 8, "Франція": 38, "Британія": 24},
        "XS": {"Німеччина": 38, "США": 10, "Франція": 40, "Британія": 26},
        "S": {"Німеччина": 40, "США": 12, "Франція": 42, "Британія": 28},
        "M": {"Німеччина": 42, "США": 14, "Франція": 44, "Британія": 30},
        "L": {"Німеччина": 44, "США": 16, "Франція": 46, "Британія": 32},
        "XL": {"Німеччина": 46, "США": 18, "Франція": 48, "Британія": 34},
        "XXL": {"Німеччина": 48, "США": 20, "Франція": 50, "Британія": 36},
        "XXXL": {"Німеччина": 50, "США": 22, "Франція": 52, "Британія": 38},
    }

    if міжнародний_розмір in розміри_переклад:
        return розміри_переклад[міжнародний_розмір]
    else:
        return "Розмір не знайдено"

міжнародний_розмір = "S"
результат = перекласти_розмір_жіночої_білизни(міжнародний_розмір)
print(f"Міжнародний розмір жіночої білизни {міжнародний_розмір} відповідає розмірам: 'Німеччина' {результат['Німеччина']}, Франція {результат['Франція']}, Британія {результат['Британія']}")
