from math import *

n, a = input(), input().split()

a = [int(x) for x in a]
a.sort()
for i in range(int(n)):
    for j in range(i + 1, int(n)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])