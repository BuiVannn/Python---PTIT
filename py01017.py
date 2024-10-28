t = int(input())

while t != 0:
    s = input()
    ans = ""
    a = s[0]
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            a = str(cnt) + a
            ans += a
            a = s[i]
            cnt = 1
    a = str(cnt) + a
    ans += a
    print(ans)
    t -= 1