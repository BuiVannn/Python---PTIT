t = int(input())

while t != 0:
    n = int(input())
    if n % 2 == 0:
        ans = 0.0
        for i in range(2, n + 1, 2):
            ans += 1/i
        print("{:.6f}".format(ans))
    else:
        ans = 1.0
        for i in range(3, n + 1, 2):
            ans += 1 / i
        print("{:.6f}".format(ans))
    t -= 1