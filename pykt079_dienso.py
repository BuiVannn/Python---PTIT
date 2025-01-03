t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mi,ma = 1e9, -1e9
    for i in a:
        if mi > i:
            mi = i
        if ma < i:
            ma = i
    cnt = 0
    for i in range(mi, ma + 1):
        if (i not in a):
            cnt += 1
    print(cnt)