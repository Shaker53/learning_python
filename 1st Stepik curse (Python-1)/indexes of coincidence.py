a = [int(i) for i in input().split()]
x = int(input())
b = []
for i in range(len(a)):
    if a[i] == x:
        b.append(i)
if len(b) > 0:
    print(*b)
else:
    print('Отсутствует')
