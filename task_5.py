rating = [9, 8, 8, 7, 6, 6, 6, 5, 3, 2, 1]

while True:
    try:
        print(f"Рейтинг = {rating}")
        user_rate = int(input("Введите новый рейтинг >>> "))
        current_rate_count = rating.count(user_rate)

        if current_rate_count:
            last_current_idx = rating.index(user_rate) + current_rate_count
            rating.insert(last_current_idx, user_rate)
        else:
            if user_rate > rating[0]:
                rating.insert(0, user_rate)
            elif user_rate < rating[-1]:
                rating.append(user_rate)
            else:
                for idx, rate in enumerate(rating):
                    if rate < user_rate:
                        rating.insert(idx, user_rate)
                        break

        print(rating)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()