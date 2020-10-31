import re
import requests

sites = set()
start_url = input().strip()
res = requests.get(start_url)
pattern = r'<a.*?href=[\'"].*?(([\w-]+\.)+\w+).*?[\'"].*?>'
all_inclusions = re.findall(pattern, res.text)
for i in all_inclusions:
    if not i[0].endswith('.html'):
        sites.add(i[0])
sites = sorted(list(sites))
for k in sites:
    print(k)