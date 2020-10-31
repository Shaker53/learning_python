import simplecrypt

text = []
with open("/home/ilya/PycharmProjects/Learning-Python1/some_files/passwords.txt") as inf:
    for line in inf:
        text += line.strip().split()
print(text)


with open("/home/ilya/PycharmProjects/Learning-Python1/some_files/encrypted.bin", "rb") as inp:
    encrypted = inp.read()



    for password in text:
        try:
            ans = simplecrypt.decrypt(password, encrypted)
        except simplecrypt.DecryptionException:
            print('.')
        else:
            print(ans)
