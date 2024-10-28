import math
def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nto = []

for i in range(2, 8000):
    if nt(i):
        nto.append(i)
n, m = map(int, input().split())

x = m
print(x, end=' ')
for i in range(n):
    print(x + nto[i], end=' ')
    x += nto[i]
    



