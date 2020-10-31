commands = []
x = 0
y = 0
n = int(input())
for i in range(n):
    commands.append(input().split())
for i in commands:
    if i[0] == 'север':
        y += int(i[1])
    elif i[0] == 'юг':
        y -= int(i[1])
    elif i[0] == 'восток':
        x += int(i[1])
    elif i[0] == 'запад':
        x -= int(i[1])
print(x, y)