t = int(input())

while t != 0:
    n = input()
    ok = 1
    for i in n:
        if i != '4' and i != '7':
            ok = 0
            break
    if ok == 1:
        print("YES")
    else: print("NO")
    t -= 1