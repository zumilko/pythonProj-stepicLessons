def get_key(d_words, value):  # ключ по значению из словаря
    for k, v in d_words.items():
        if v == value:
            return k


if __name__ == '__main__':
    with open("in2.txt", "r") as input_file:
        words = input_file.read().lower().split()  # список слов (типа строка) из файла
        d: dict = {i: words.count(i) for i in words}  # генерация словаря: ключ - слово, значение - количество
        m = max(d.values())

    with open("out2.txt", "w") as output_file:
        output_file.write(f"{get_key(d, m)} {m}")
