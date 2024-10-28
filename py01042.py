t = int(input())

while t != 0:
    n = input()
    ok = 1
    for i in n:
        if i != '1' and i != '2' and i != '0':
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1