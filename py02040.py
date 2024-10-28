from math import *


n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]
b = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

k = int(input())
#for i in range(n):
#    for j in range(n):
#        a[i][j] = b[j][i]

#for i in range(n):
 #   for j in range(n):
     #   print(a[i][j], end=" ")
    #print()

s1 = 0
s2 = 0
for i in range(n - 1):
    for j in range(0, n - i - 1):
        s1 += a[i][j]
        #print(a[i][j], end=" ")
    #print()
for i in range(n - 1, 0, -1):
    for j in range(n - i, n):
        s2 += a[i][j]
        #print(a[i][j], end=" ")
    #print()

#print(s1)
#print(s2)
if abs(s1 - s2) <= k:
    print("YES")
else:
    print("NO")
print(abs(s1 - s2))
