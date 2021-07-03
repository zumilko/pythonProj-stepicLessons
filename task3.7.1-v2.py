'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''
 #  попробовать генератор для ввода [input().strip().split(';') for i in range(int(input()))]
data = list(iter(input, ''))  # ; print(data) # список из строк ввода
data = [data[i].split(';') for i in range(1, len(data))]
team = {data[i][0]: [1, 1, 0, 0, 3] if int(data[i][1]) > int(data[i][3]) else [1, 0, 0, 1, 0] for i in range(len(data))}
# ames = {'game' + str(i): data[i].split(';') for i in range(1, len(data))} # генератор словаря, 1е число не брать
print(f"{data}\n")
print(team)