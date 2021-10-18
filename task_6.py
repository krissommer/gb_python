def int_func(input_word: str):
    return "".join([
        input_word[0].upper(), input_word[1:]
    ])

user_words = input("Введите строку из нескольких слов >>> ").split()
user_words = [int_func(x) for x in user_words]

print(" ".join(user_words))