import sys
sys.stdin = open('text.txt', 'r')
f = sys.stdin



m = []
while 1:
    a = map(int, f.readline().split())