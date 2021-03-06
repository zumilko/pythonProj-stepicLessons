# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием
# модуля requests и посчитать число строк в нём.
# Используйте функцию get для получения файла (имеет смысл вызвать метод strip к
# передаваемому параметру, чтобы убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю text.
# Если результат работы скрипта не принимается, проверьте поле url на правильность.
# Для подсчёта количества строк разбейте текст с помощью метода splitlines.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests
with open('dataset_3378_2.txt', 'r') as input_file:
    r = requests.get(input_file.read().strip())
    print(len(r.text.splitlines()))
    #print(list(filter(None, r.text.strip().splitlines())))  # filter(None, testList) -способ удаления пустых строк
    # пустые строки для выполнения задания не удалять!
    # Удаление пустых строк и их подсчёт:
    # count = 0
    # while "" in rlist:
    #     rlist.remove("")
    #     count += 1
    # print(rlist,'\n', count)
    rlist = r.text.splitlines()
    c = 0
    for line in rlist:
        c += 1
    print(c)

