a = []
while 1:
    b = input().split()
    if b == ['end']:
        break
    a.append(b)
ans = [['0' for j in range(len(a[0]))] for i in range(len(a))]
for i in range(len(a)):
    for j in range(len(a[0])):
        ans[i][j] = int(a[i - 1][j]) + int(a[(i + 1) % len(a)][j]) + int(a[i][j - 1]) + int(a[i][(j + 1) % len(a[0])])
        print(ans[i][j], end=' ')
    print()
