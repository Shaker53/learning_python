import re
import requests

start_url = input()
finish_url = input()
counter = 0

res = requests.get(start_url)
pattern = r'<a.*?href="(.*?)">'
all_inclusions = re.findall(pattern, res.text)

for inclusion in all_inclusions:
    res2 = requests.get(inclusion)
    if res2.status_code == 200:
        all_incls_2 = re.findall(pattern, res2.text)
        if finish_url in all_incls_2:
            counter = 1
            break
if counter == 0:
    print('No')
else:
    print('Yes')
