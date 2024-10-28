
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    
    for i in range(m):
        c = []
        for j in range(n):
            c.append(a[j][i])
        b.append(c)
    
    ans = []
    for i in range(n):
        row = []
        for j in range(n):
            s = 0
            for k in range(m):
                s += a[i][k] * b[k][j]
            row.append(s)
        ans.append(row)
    
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()
            
