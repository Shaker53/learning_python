import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*?(cat.*?){2,}.*?'
    x = re.match(pattern, line)
    if x:
        print(line)