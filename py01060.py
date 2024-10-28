
def solve(n):
    su = 0
    tich = 1
    ok = 0
    for i in range(len(n)):
        if int(i) % 2 != 0:
            su += int(n[i])
        else:
            if int(n[i]) != 0:
                ok = 1
    if ok == 0:
        tich = 0
    else:
        for i in range(len(n)):
            if int(i) % 2 == 0 and int(n[i]) != 0:
                tich *= int(n[i])
    return (su, tich)

for _ in range(int(input())):
    n = input()
    a, b = solve(n)
    print(b, a)