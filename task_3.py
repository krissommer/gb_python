my_dict = {}


def get_data(lines: str, min_value=20000.0):
    for line in lines:
        tmp_list = line.split()
        my_dict[tmp_list[0]] = float(tmp_list[1])
    print(f"Средняя зарплата = {sum(my_dict.values()) / len(my_dict)}")
    print(f"Зарплата менее {min_value} у следующих сотрудников:")
    for k, v in my_dict.items():
        if v < min_value:
            print(k)


with open("text_3.txt", encoding="utf-8") as f:
    get_data(f.read().split("\n"))