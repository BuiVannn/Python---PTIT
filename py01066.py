def check(s):
    s1 = s[::-1]
    for i in range(1, len(s)):
        n = abs(ord(s[i]) - ord(s[i - 1]))
        m = abs(ord(s1[i]) - ord(s1[i - 1]))
        if n != m:
            return 0
    return 1

for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")