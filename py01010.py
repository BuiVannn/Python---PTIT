t = int(input())

while t != 0:
    s = input()
    n = len(s)
    if (s[0] == s[n - 2]) and (s[1] == s[n - 1]):
        print("YES")
    else: print("NO")
    #print(n)
    t -= 1