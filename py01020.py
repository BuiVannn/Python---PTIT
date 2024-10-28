t = int(input())

while t != 0:
    s = input()
    ans = s[len(s) - 2] + s[len(s) - 1]
    if ans == '86':
        print("YES")
    else:
        print("NO")
    t-=1