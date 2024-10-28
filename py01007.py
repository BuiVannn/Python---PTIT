t = int(input())

while t != 0:
    n, x, m = input().split()
    n = float(n)
    x = float(x)
    m = float(m)
    #print(type(n), type(x), type(m))
    cnt = 0
    stht = n
    while stht < m:
        lai = stht * x / 100
        stht += lai
        cnt += 1
    print(cnt)
    t -= 1