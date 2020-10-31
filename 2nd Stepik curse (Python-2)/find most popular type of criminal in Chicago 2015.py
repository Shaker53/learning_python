import csv
import re

all_2015 = []
pattern = r'.*?/2015 .*?'
with open("crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        match = re.match(pattern, row[2])
        if match:
            all_2015.append(row[5])
types = set(all_2015)
dict = {}
for type in types:
    dict[type] = 0
for i in all_2015:
    dict[i] += 1
list = list(dict.items())
list.sort(key=lambda k: k[1])
print(list[-1][0])
