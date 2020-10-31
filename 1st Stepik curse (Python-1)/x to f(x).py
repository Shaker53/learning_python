n = int(input())
dict = {}
stroka = []
for i in range(n):
    x = int(input())
    stroka.append(x)
for key in stroka:
    if key not in dict:
        dict[key] = f(key)
for j in stroka:
    print(dict[j])
