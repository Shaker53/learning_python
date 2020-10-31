import requests
with open("/home/asd/Desktop/test_input.txt") as inf:
    link = inf.readline()
print(link)
r = requests.get(link.strip())
while r.text.split()[0] != 'We':
    r = requests.get(('https://stepic.org/media/attachments/course67/3.6.3/' + r.text).strip())
with open('/home/asd/Desktop/test_output.txt', 'w') as ouf:
    ouf.write(r.text)
