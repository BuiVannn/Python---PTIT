

for t in range(int(input())):
    n = input()
    a = n[0]
    ok = 1
    for i in range(2, len(n) - 1, 2):
        if n[i] != a:
            ok = 0
    #print(ok)
    if ok == 1 and len(n) % 2 != 0 and n[0] != n[1]:
        print("YES")
    else:
        print("NO")