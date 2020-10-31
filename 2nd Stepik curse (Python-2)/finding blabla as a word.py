import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*?\b(\w+)\1\b.*?'
    x = re.match(pattern, line)
    if x:
        print(line)