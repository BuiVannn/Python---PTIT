from math import sqrt

def nt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

n, a = int(input()), input().split()
a = [int(x) for x in a]

#a.sort()
d = dict({})

for i in a:
    if i in d:
        d[i] += 1
    else:
        if nt(i):
            d[i] = 1
for i in d:
    print(i, d[i])