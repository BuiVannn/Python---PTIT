t = int(input())

while t != 0:
    n = input()
    ans = 1
    for i in n:
        if int(i) != 0:
            ans *= int(i)
    print(ans)
    t -= 1