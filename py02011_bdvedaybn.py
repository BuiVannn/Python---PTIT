import math
n = int(input())

a = list(map(int, input().split()))
ans = []
for i in range(n):
    s = 0
    for j in range(n):
        if j != i:
            s += abs(a[i] - a[j])
    ans.append(s)

m = 1e9
for i in range(n):
    if m > ans[i]:
        m = ans[i]

for i in range(n):
    if m == ans[i]:
        print(f'{m} {a[i]}')
        break