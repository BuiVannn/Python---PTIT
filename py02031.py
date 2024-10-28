from math import sqrt

def nt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

n, m = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print("")