origin = input()
cipher = input()
origin_in = input()
cipher_in = input()
for i in origin_in:
    print(cipher[origin.find(i)], end='')
print()
for i in cipher_in:
    print(origin[cipher.find(i)], end='')