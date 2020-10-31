a = int(input())
b = int(input())
nok = 1
while nok % a != 0 or nok % b != 0:
    nok +=1
print(nok)