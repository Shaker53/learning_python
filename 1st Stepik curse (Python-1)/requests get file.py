import requests
with open("/home/asd/Desktop/test_input.txt") as inf:
    link = inf.readline()
print(link)
r = requests.get(link.strip())
print(r.text)
r = r.text.splitlines()
print(str(r))
print(len(r))