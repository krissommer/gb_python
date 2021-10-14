items = input("Укажите значения списка через запятую >>> ").split(",")

max_idx = len(items) - 1

for idx in range(0, max_idx, 2):
    next_idx = idx + 1
    items[idx], items[next_idx] = items[next_idx], items[idx]

print(items)