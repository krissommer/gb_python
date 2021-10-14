month = int(input("Укажите номер месяца >>> "))

year_dict = {
    "зима": (12, 1, 2),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11),
}

for season, months in year_dict.items():
    if month in months:
        print(f"Время года = {season}")
        break