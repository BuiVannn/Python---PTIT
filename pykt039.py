
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ok = 1
    for i in range(n):
        if a[i] > b[i] :
            ok = 0
            break
    if ok == 1:
        print("YES")
    else:
        print("NO")
