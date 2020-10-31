with open("/home/asd/Desktop/test_input.txt") as inf:
    line = inf.readline()
line += '*'
out =''
k = 0
num = 0
letter = 0
end = 0
while line[k] != '*':
    if '0' <= line[k] <= '9':
        if num == 0:
            num = int(line[k])
        else:
            num = num * 10 + int(line[k])
        if line[k + 1] > '9' or line[k + 1] < '0':
            end = 1
        k += 1
    else:
        letter = line[k]
        k += 1
    if end == 1:
        out += letter * num
        end = 0
        num = 0
        letter = 0
with open('/home/asd/Desktop/test_output.txt', 'w') as ouf:
    ouf.write(out)