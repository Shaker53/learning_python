import os
import os.path
a = []
for current_dir, dirs, files in os.walk("/home/asd/Desktop/main"):
    for file in files:
        if '.py' in file:
            a.append(current_dir[current_dir.find('main'):] + '\n')
a = set(a)
a = list(a)
print(a)
a.sort()
print(a)
with open ('test_output.txt', 'w') as w:
    for i in a:
        w.write(i)