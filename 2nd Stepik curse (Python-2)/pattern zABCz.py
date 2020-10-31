import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*?z.{3}z.*?'
    x = re.match(pattern, line)
    print(x)
    if x:
        print(line)