
for t in range(int(input())):
    s1 = input()
    s2 = input()
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    ok = 1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ok = 0
            break
    print("Test " + str(t + 1) + ": ", end="")
    if ok:
        print("YES")
    else:
        print("NO")