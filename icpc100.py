
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(1, len(a)):
        be = min(a[i - 1], a[i])
        lon = max(a[i - 1], a[i])
        if(lon > be * 2):
            while lon > be * 2:
                x = lon / 2
                cnt += 1
                if x - int(x) == 0:
                    lon = x
                else:
                    lon = int(x) + 1
    print(cnt)
            