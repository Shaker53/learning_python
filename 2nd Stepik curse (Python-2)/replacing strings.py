s = input()
a = input()
b = input()
counter = 0
if a in b and a in s:
    print('Impossible')
else:
    while 1:
        if a in s:
            s = s.replace(a, b)
            counter += 1
            if counter >= 1000:
                print('Impossible')
                break
        else:
            print(counter)
            break

