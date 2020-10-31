import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(\W*)(\w)(\w)(.*?)\b'
    x = re.sub(pattern, r'\1\3\2\4', line)
    print(x)