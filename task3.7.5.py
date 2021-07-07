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
    for item in data:
        item[0] = int(item[0])
        item[2] = int(item[2])


def count_val(dict_, test_summ_all=0):
# Выводит количество значений в списке для каждого ключа
# и считает общую сумму значений в словаре для проверки:
    for key in group:
        test_summ_all += len(group[key])
        print(f"class-{key}: {len(group[key])}, ")
    return test_summ_all

height = 0
group = {}
group_count = 0
test_summ_all = 0

# Читать данные из файла этого формата в виде вложенного списка:
with open('dataset_3380_5.txt', 'r') as input_file:
    data = [row.split() for row in input_file.readlines()]
prepare(data)

# Создать словарь ключ - класс,
# значение - список ростов учеников класса:
for rec in data:
    group.setdefault(rec[0], []).append(rec[2])


def average_height(group_):
    height_ = 0
    for key in group_:
        all_height = 0
        for item in group_[key]:
            all_height += item
        aver_all_height = height_ / len(group_[key])
        return aver_all_height


print(f"{group}\nчисло групп (классов): {len(group)}")
print(f"исходных данных {len(data)},"
      f" данных в словаре {count_val(group)}")
print(data)

print(average_height(group))

for key in group:
    all_h = 0
    for item in group[key]:
        all_h += item
    aver_all_h = all_h / len(group[key])

    print(f"{key}, {group[key]}, {all_h}, {aver_all_h}")
