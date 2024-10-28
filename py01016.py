t = int(input())

while t != 0:
    s = input()
    ans = ""
    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]
        else:
            n = int(s[i])
            for k in range(n - 1):
                ans += s[i - 1]
    print(ans)
    t -= 1