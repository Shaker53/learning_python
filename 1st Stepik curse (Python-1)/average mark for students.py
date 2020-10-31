s = []
out = ''
out_stud = []
out_math, out_phys, out_russ = 0, 0, 0
with open("/home/ilya/Desktop/test_input.txt") as inf:
    for line in inf:
        s.append(line.strip().split(';'))
print(s)
for i in range(len(s)):
    out_stud += str((int(s[i][1]) + int(s[i][2]) + int(s[i][3])) / 3).split(' ')
    out_math += int(s[i][1])
    out_phys += int(s[i][2])
    out_russ += int(s[i][3])
print(out_stud)
print(out_math)
print(out_phys)
print(out_russ)
out = str(out_math / len(s)) + ' ', str(out_phys / len(s)) + ' ', str(out_russ / len(s)) + ' '
with open('/home/ilya/Desktop/test_output.txt', 'w') as ouf:
    for i in range(len(out_stud)):
        ouf.write(out_stud[i])
        ouf.write('\n')
    ouf.write(out[0])
    ouf.write(out[1])
    ouf.write(out[2])
