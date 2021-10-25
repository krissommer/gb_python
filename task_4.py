russian_dict = {
    1: "Один",
    2: "Два",
    3: "Три",
    4: "Четыре",
    5: "Пять",
    6: "Шесть",
    7: "Семь",
    8: "Восемь",
    9: "Девять",
    10: "Десять"
}

with open("result_text_4.txt", "w", encoding="utf-8") as f_out:
    with open("text_4.txt", "r", encoding="utf-8") as f_input:
        for line in f_input:
            f_out.write(f'{russian_dict.get(int(line.split(" - ")[1]))} - {line.split(" - ")[1]}')