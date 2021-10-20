numbers = [22, 1, 90, 1, 23, 1, 44, 1, 3, 2, 15, 7, 7, 90]

items = [x for x in numbers if numbers.count(x) == 1]

print(items)