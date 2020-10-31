table = []
dict = {}
with open("/home/asd/Desktop/test_input.txt") as inf:
    for line in inf:
        table.append(line.strip().split())
for i in range(1, 12):
    dict[i] = [0, 0]
for i in table:
    dict[int(i[0])][0] = dict[int(i[0])][0] + int(i[2])
    dict[int(i[0])][1] += 1
for i in range(1, 12):
    if dict[i][0] == 0:
        dict[i] = '-'
    else:
        dict[i] = dict[i][0] / dict[i][1]
for i in range(1, 12):
    print(i, dict[i])