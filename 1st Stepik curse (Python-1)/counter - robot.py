a = int(input())
if 11 <= a % 100 <= 14 or a % 10 == 0 or 5 <= a % 10 <= 9:
    print(a, 'программистов')
else:
    if a % 10 == 1:
        print(a, 'программист')
    elif 2 <= a % 10 <= 4:
        print(a, 'программиста')