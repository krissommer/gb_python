numbers = [80, 60, 4, 22, 1, 0, 4, 8, 8, 1, 78, 360, 35]

result_list = [
    val for idx, val in enumerate(numbers)
    if idx > 0 and numbers[idx - 1] < val
]

print(result_list)