from math import *


n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(i + 1, n):
        s1 += a[i][j]

for i in range(1, n):
    for j in range(0, i):
        s2 += a[i][j]

if abs(s1 - s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1 - s2))
