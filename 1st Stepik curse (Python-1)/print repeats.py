a = [int(i) for i in input().split()]
a.sort()
a += '!'
s = ''
cnt = 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        cnt += 1
    else:
        if cnt != 1:
            print(a[i], end= ' ')
        cnt = 1