def c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c(n - 1, k) + c(n - 1, k - 1)


n, k = map(int, input().split())
ans = c(n, k)
print(ans)
