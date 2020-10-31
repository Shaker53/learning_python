import itertools

def primes():
    a = 1
    while 1:
        i = 0
        a += 1
        for k in range(2, a):
            if a % k == 0:
                i += 1
        if i == 0:
            yield a



print(list(itertools.takewhile(lambda x: x <= 31, primes())))