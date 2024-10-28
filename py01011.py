t = int(input())

while t != 0:
    n = int(input())
    for i in range(n):
        s = str(i)
        u = s[::-1]
        ok = 1
        for k in s:
            if k != '0' and k != '2' and k != '4' and k != '6' and k != '8':
                ok = 0
        if s == u and ok and len(s) >= 2:
            print(s + ' ', end='')
    t -= 1