gen = input()
gen += '0'
s = ''
cnt = 1
for i in range(len(gen) - 1):
    if gen[i] == gen[i + 1]:
        cnt += 1
    else:
        s += str(gen[i]) + str(cnt)
        cnt = 1
print(s)