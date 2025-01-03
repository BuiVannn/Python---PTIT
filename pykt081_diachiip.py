t = int(input())

for _ in range(t):
    try:
        ok = 1
        ip = list(map(int, input().split('.')))
        if len(ip) != 4:
            ok = 0
        for i in ip:
            if i < 0 or i > 255:
                ok = 0
                break
        if ok == 1:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")