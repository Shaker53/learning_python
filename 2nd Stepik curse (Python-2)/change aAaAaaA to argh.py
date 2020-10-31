import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\ba+\b'
    x = re.sub(pattern, 'argh', line, 1, re.IGNORECASE)
    print(x)