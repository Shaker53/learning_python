n = int(input())
a = []
k = 1
while 1:
    for i in range(k):
        if len(a) >= n:
            break
        a.append(k)
    k += 1
    if len(a) >= n:
        break
print(*a)
