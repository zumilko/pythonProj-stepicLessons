#  Copyright (c) 2021.  Primus-E
"""
Дан файл с таблицей в формате TSV с информацией о росте школьников разных
классов. Напишите программу, которая прочитает этот файл и подсчитает для
каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет
собой три поля: Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов,
а в качестве роста используется натуральное число, но при подсчёте
среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания
номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него
прочерк. В качестве ответа прикрепите файл с полученными данными
о среднем росте.

Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0

"""


def prepare(list_):
    """
    Функция приводит к целому типу определённые поля в данных:
    :param list_: данные в виде вложенного списка
    :return: None
    """
    for elm in list_:
        elm[0] = int(elm[0])
        elm[2] = int(elm[2])


def count_val(dict_, test_summ_all=0):
    """
    Функция выводит количество значений в списке для каждого ключа и
    считает общую сумму значений в словаре, для проверки корректности
    упаковки исходных данных из списка в словарь:
    :param dict_:  словарь с исходными данными.
    :param test_summ_all: сумма количества записей из данных в словаре.
    """
    for key in dict_:
        test_summ_all += len(dict_[key])
        print(f"class-{key}: {len(dict_[key])}, ")
    return test_summ_all


def average_val(list_, aver_height=0):
    """
    Функция должна вычислить среднее от значений в числовом списке.
    :param list_: список с цифровыми значениями
    :param aver_height: результат
    """
    try:
        height = 0
        for item in list_:
            height += item
        aver_height = height / len(list_)
        return aver_height
    except TypeError:
        return '-'


group = {}

# Читать данные из файла этого формата в виде вложенного списка:
with open('dataset_3380_5.txt', 'r') as input_file:
    data = [row.split() for row in input_file.readlines()]
prepare(data)

# Создать словарь ключ - класс,
# значение - список ростов учеников класса:
for rec in data:
    group.setdefault(rec[0], []).append(rec[2])

# Вывод результата в сортированном по ключу виде:
for k in range(1,12):
    print(k, average_val(group.get(k)))

# Тестовые принты:
# print(f"{group}\nчисло групп (классов): {len(group)}")
# print(f"исходных данных {len(data)},"
#       f" данных в словаре {count_val(group)}")
# print(data)
