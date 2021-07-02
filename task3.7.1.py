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
games = {}
teams = {}
game = ''

for j in range(int(input())):  # в range считывается первая цифра = число строк ввода
    game = input().strip().split(';')  # далее по одной строке и делится на список с результатом одной игры
    j += 1
    key = 'game_' + str(j)
    games[key] = game  # просто сохранение всех списков игр в словарь
print(game)
# генератор вложенного словаря с нач. значениями для всех team из games
teams = {games[key][t]: {'play': 0, 'win': 0, 'draw': 0, 'loss': 0, 'points': 0} for t in (0, 2) for key in games}

for key in games:
    if int(games[key][1]) > int(games[key][3]):
        teams[games[key][0]]['play'] += 1
        teams[games[key][0]]['win'] += 1
        teams[games[key][0]]['points'] += 3
        teams[games[key][2]]['play'] += 1
        teams[games[key][2]]['loss'] += 1
    if int(games[key][1]) < int(games[key][3]):
        teams[games[key][2]]['play'] += 1
        teams[games[key][2]]['win'] += 1
        teams[games[key][2]]['points'] += 3
        teams[games[key][0]]['play'] += 1
        teams[games[key][0]]['loss'] += 1
    if int(games[key][1]) == int(games[key][3]):
        teams[games[key][2]]['play'] += 1
        teams[games[key][2]]['draw'] += 1
        teams[games[key][2]]['points'] += 1
        teams[games[key][0]]['play'] += 1
        teams[games[key][0]]['draw'] += 1
        teams[games[key][0]]['points'] += 1

for k in teams:
    print(f"{k}:{teams[k]['play']} {teams[k]['win']} {teams[k]['draw']} {teams[k]['loss']} {teams[k]['points']}")
