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

play, win, draw, loss, points = 0, 0, 0, 0, 0
total = {'play': play, 'win': win, 'draw': draw, 'loss': loss, 'points': points}
team = {}
game, name = '', ''
games = dict()

for j in range(int(input())):  # в range считывается первая цифра = число строк ввода
    game = input().strip().split(';') # ; print(f"{game}") # результат одной игры в списке
    j += 1
    key = 'game_' + str(j)
    games[key] = game
    print(game)
    team[game[0]] = total
    team[game[2]] = total
    if int(game[1]) > int(game[3]):
        team[game[0]]['play'] += 1
        team[game[0]]['win'] += 1
        team[game[0]]['points'] += 3
        team[game[2]]['loss'] += 1
    # if int(game[1]) < int(game[3]):
        # team[game[0]] = {'play': play + 1, 'win': win}
        # team[game[2]] = {'play': play + 1, 'loss': loss}
print(team)
# print(f"\n{games}")
# for key in games:
#     if int(games[key][1]) > int(games[key][3]):
#         team[games[key][0]]['play'] += 1
#         team[games[key][0]]['win'] += 1
#         team[games[key][0]]['points'] += 3

#    if int(games[key][1]) < int(games[key][3]):

#print(games)
# team[str([x for i, x in enumerate(games[key], 1) if i == 1])] = total
# team[str([x for i, x in enumerate(games[key], 1) if i == 3])] = total
# print(total, team)

#games = {x : {'p': j, 'w': 1} if int(game[1]) > int(game[3]) else {'p': i, 'loss': 1} for i, x in enumerate(game) if i % 2 == 0}