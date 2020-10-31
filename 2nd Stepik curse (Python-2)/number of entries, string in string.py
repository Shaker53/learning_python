s = input()
t = input()
counter = 0
start = 0
while 1:
    a = s.find(t, start)
    if a == -1:
        print(counter)
        break
    else:
        counter += 1
        start = a + 1