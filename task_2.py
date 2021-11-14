class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите делимое и делитель через пробел: ").split()

try:
    numerator = int(inp_data[0])
    denominator = int(inp_data[1])
    if denominator == 0:
        raise OwnError("Вы ввели нуль, на него делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше результат: {numerator / denominator}")