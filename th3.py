n, m = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

mi = a[0][0]
ma = a[0][0]

for i in range(n):
    for j in range(m):
        if a[i][j] < mi:
            mi = a[i][j]
        if a[i][j] > ma:
            ma = a[i][j]

x = ma - mi
