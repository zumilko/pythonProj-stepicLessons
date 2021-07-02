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

team = {}; games = {}
game = ''

for j in range(int(input())):  # в range считывается первая цифра = число строк ввода
    game = input().strip().split(';') # ; print(f"{game}") # результат одной игры в списке
    j += 1
    key = 'game_' + str(j)
    games[key] = game

print(f"\n{games}")
for key in games:
    k = games[key][0]
    team[k] = {'play': 0}
    team[k] |= {'win' : 0}
    team[k] |= {'draw': 0}
    team[k] |= {'loss': 0}
    team[k] |= {'points': 0}
    k = games[key][2]
    team[k] = {'play': 0}
    team[k] |= {'win': 0}
    team[k] |= {'draw': 0}
    team[k] |= {'loss': 0}
    team[k] |= {'points': 0}
for key in games:
    if int(games[key][1]) > int(games[key][3]):
        team[games[key][0]]['play'] += 1
        team[games[key][0]]['win'] += 1
        team[games[key][0]]['points'] += 3
        team[games[key][2]]['play'] += 1
        team[games[key][2]]['loss'] += 1
    if int(games[key][1]) < int(games[key][3]):
        team[games[key][2]]['play'] += 1
        team[games[key][2]]['win'] += 1
        team[games[key][2]]['points'] += 3
        team[games[key][0]]['play'] += 1
        team[games[key][0]]['loss'] += 1
    if int(games[key][1]) == int(games[key][3]):
        team[games[key][2]]['play'] += 1
        team[games[key][2]]['draw'] += 1
        team[games[key][2]]['points'] += 1
        team[games[key][0]]['play'] += 1
        team[games[key][0]]['draw'] += 1
        team[games[key][0]]['points'] += 1
print(f"\n{team}")
for k in team:
    print(f"{k}:{team[k]['play']} {team[k]['win']} {team[k]['draw']} {team[k]['loss']} {team[k]['points']}")