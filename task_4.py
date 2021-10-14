words = input("Введите строку из нескольких слов >>> ").split()

for idx, value in enumerate(words, start=1):
    print(f"{idx}. {value[:10]}")