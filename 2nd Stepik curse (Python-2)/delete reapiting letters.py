import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(.*?)((\w)\3+)(.*?)'
    x = re.sub(pattern, r'\1\3\4', line)
    print(x)