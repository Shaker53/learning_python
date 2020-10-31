a = int(input())
b = int(input())
c = int(input())
if b > a:
    a , b = b , a
if c > a:
    a , c = c, a
if c < b :
    b , c = c, b
print(a)
print(b)
print(c)