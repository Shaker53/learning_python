dict = []
text = ()
mistakes = ()
d = int(input())
for i in range(d):
    dict.append(input().lower())
l = int(input())
for i in range(l):
    text += tuple(input().lower().split())
for i in text:
    if i not in dict:
        mistakes += tuple(i.split())
for i in set(mistakes):
    print(i)