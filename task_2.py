my_dict = {"Всего строк:": 0, "Всего слов:": 0}
with open("task_2.txt", "r", encoding="utf-8") as f:
    num_lines = 1
    for line in f:
        if line:
            my_dict["Всего строк:"] += 1
            word_count = len(line.split())
            print(f"В {num_lines} строке - {word_count} слов(о, а)")
            my_dict["Всего слов:"] += word_count
            num_lines += 1

for k, v in my_dict.items():
    print(k, v, end=" ")