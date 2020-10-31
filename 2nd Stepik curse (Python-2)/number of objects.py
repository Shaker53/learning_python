ans = 0
sum = []
for obj in objects:
    if obj not in sum:
        ans += 1
        sum.append(obj)
print(ans)