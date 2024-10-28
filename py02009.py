from math import *


for _ in range(int(input())):
    n = int(input())
    c = dict({})
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
        if a[i] in c:
            c[a[i]] += 1
        else:
            c[a[i]] = 1
    
    d = sorted(c, key=lambda x : (-c[x], x))
    print(d[0])
