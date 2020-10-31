import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(1(01*0)*1|0)*'
    x = re.fullmatch(pattern, line)
    if x:
        print(line)