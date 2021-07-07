#  Copyright (c) 2021.  Primus-E

"""
Генераторы
"""
# This function generated dictionary with key in range.
# sample: {'1': [], '2': [], '3': []}
a = dict.fromkeys((str(i) for i in range(1, 12)), [])
print(a)

sample_data = [['7', 'Simon', 159], ['2', 'Jones', 127],
               ['2', 'Miller', 130], ['8', 'Milton', 163],
               ['8', 'Bargeman', 161]]
b = {i[1] + '-class' + i[0]: {i[0]: i[2]} for i in sample_data}
print(b)