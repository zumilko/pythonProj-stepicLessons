# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests
with open('dataset_3378_3.txt', 'r') as input_file:
    link = input_file.read().strip()
    txt = requests.get(link).text.strip()
    count = 0 # счётчик для информации
    while 'We' not in txt:
        link_sp = link.split('3.6.3/')
        txt = requests.get(link).text.strip()
        link_next = link_sp[0] + '3.6.3/' + txt
        link = link_next
        count += 1 # счётчик для информации
        print(count, link_sp, link_next) # контроль выполнения
    print(f"\nОтвет: \n{txt}")



