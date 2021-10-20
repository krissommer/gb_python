from sys import argv

app_Name, work_time, rate, *prize = argv
try:
    work_time = float(work_time)
    rate = float(rate)
except ValueError:
    print("Ошибка входных данных")
else:
    if prize:
        try:
            bonus = list(map(float, prize))
        except ValueError:
            print("Ошибка входных данных премии")
        else:
            print(work_time * rate + sum(bonus))
    else:
        print(work_time*rate)
