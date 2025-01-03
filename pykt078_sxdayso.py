t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ma = -1e9
    idx = -1
    for i in range(n):
        if a[i] > ma:
            ma = a[i]
            idx = i
    for i in range(n):
        if a[i] == ma:
            idx = i
            break
    

    b = []
    c = []
    for i in range(idx):
        if a[i] < 0:
            b.append(a[i])
        else:
            c.append(a[i])
    if m < 0:
        b.append(m)
    else:
        c.append(m)
    for i in range(idx, n):
        if a[i] < 0:
            b.append(a[i])
        else:
            c.append(a[i])
    for i in b:
        print(i, end=" ")
    for i in c:
        print(i, end=" ")
    print()
    