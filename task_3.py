class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
num = ""
end_input = False

print(input('Для выхода из программы нажмите "Q", для продолжения "Enter": '))
while not end_input:
    x = input("Введите число: ")
    if x.upper() == 'Q':
        end_input = True
        print(result)
    else:
        try:
            if not x.isdigit():
                raise OwnError("Необходимо вводить число!")
        except OwnError:
            print("Вы ввели не число")
        else:
            result.append(x)