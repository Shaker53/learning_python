stroka = [i for i in input().lower().split()]
dict = {}
for key in stroka:
    if key not in dict:
        dict[key] = 1
    else:
        dict[key] += 1
for items in dict.items():
    print(*items)
