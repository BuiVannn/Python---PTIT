t = int(input())

while t != 0:
    s = input()
    ok = 1
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i - 1]):
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1