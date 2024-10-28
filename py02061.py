t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n) :
        a.append(list(map(int, input().split())))
    b = []
    for i in range(3):
        b.append(list(map(int, input().split())))
    s = 0
    for i in range(n - 3 + 1):
        for j in range(m - 3 + 1):
            for u in range(3):
                for v in range(3):
                    s += a[i + u][j + v] * b[u][v]
                    
    
    print(s)
    
    
    