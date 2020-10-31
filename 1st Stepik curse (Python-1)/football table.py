n = int(input())
games = []
dict = {}
for i in range(n):
    games.append(input().split(';'))
for game in games:
    if game[0] not in dict:
        dict[game[0]] = [0, 0, 0, 0, 0]
    if game[2] not in dict:
        dict[game[2]] = [0, 0, 0, 0, 0]
    if game[1] > game[3]:

        dict[game[0]][0] += 1
        dict[game[2]][0] += 1

        dict[game[0]][1] += 1
        dict[game[0]][4] += 3

        dict[game[2]][3] += 1

    elif game[1] == game[3]:

        dict[game[0]][0] += 1
        dict[game[2]][0] += 1

        dict[game[0]][2] += 1
        dict[game[0]][4] += 1

        dict[game[2]][2] += 1
        dict[game[2]][4] += 1

    elif game[1] < game[3]:

        dict[game[0]][0] += 1
        dict[game[2]][0] += 1

        dict[game[0]][3] += 1

        dict[game[2]][1] += 1
        dict[game[2]][4] += 3
for i in dict:
    print(i + ':',end='')
    print(*dict[i])
