x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))
print(id(x[0]))
print(id([1, 2, 3][0]))

print()

a = [1, 2, 3]
b = a
print(b is a)
print(b is [1, 2, 3])

print()

k = [1, 2, 3]
l = k
print(k is l)
l.append(4)
print(str(k))
print(l)