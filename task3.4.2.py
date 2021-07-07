def get_key(d_words, value):  # ключ по значению из словаря
    for k, v in d_words.items():
        if v == value:
            return k


if __name__ == '__main__':
    with open("in2.txt", "r") as input_file:
        # Список слов (типа строка) из файла:
        words = input_file.read().lower().split()
        # Генерация словаря: ключ - слово, значение - количество:
        d: dict = {i: words.count(i) for i in words}
        m = max(d.values())

    with open("out2.txt", "w") as output_file:
        output_file.write(f"{get_key(d, m)} {m}")
