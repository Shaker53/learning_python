import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'human'
    x = re.sub(pattern, 'computer', line)
    print(x)