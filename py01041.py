
def check(n):
    for i in range(1, len(n)):
        if n[i] == n[i - 1]:
            return -1
        if n[i] < n[i - 1]:
            return i
    return -1
t = int(input())

while t != 0:
    n = input()

    ok = 1
    if len(n) < 3:
        ok = 0
    else:
        idx = check(n)
        if idx == -1:
            ok = 0
        else:
            for i in range(idx + 1, len(n)):
                if n[i] > n[i - 1]:
                    ok = 0
                    break
    if ok == 1:
        print("YES")
    else:
        print("NO")
    t -= 1