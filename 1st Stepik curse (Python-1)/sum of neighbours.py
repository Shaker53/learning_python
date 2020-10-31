a = [int(i) for i in input().split()]
b = [0] * len(a)
for i in range(len(a)):
    if len(a) == 1:
        b = a
        break
    elif i != len(a) - 1:
        b[i] = a[i - 1] + a[i + 1]
    else:
        b[i] = a[i - 1] + a[0]
for i in b:
    print(i, end= ' ')