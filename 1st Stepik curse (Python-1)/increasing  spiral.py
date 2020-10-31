n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
k = 1
circle = 1
j = 0
i = 0
while circle <= (n + 1) // 2:
    for c in range(n):
        if a[i][j] != 0:
            j += 1
            continue
        else:
            a[i][j] = k
            k += 1
            j += 1
    j -= circle
    i = 0
    for c in range(n):
        if a[i][j] != 0:
            i += 1
            continue
        else:
            a[i][j] = k

            k += 1
            i += 1
    i -= circle
    j = n - 1
    for c in range(n):
        if a[i][j] != 0:
            j -= 1
            continue
        else:
            a[i][j] = k
            k += 1
            j -= 1
    j += circle
    i = n - 1
    for c in range(n):
        if a[i][j] != 0:
            i -= 1
            continue
        else:
            a[i][j] = k
            k += 1
            i -= 1
    i = i + circle + 1
    circle +=1
    j = 0
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()