import math
t = int(input())

while t != 0:
    s = input()
    ok1 = 1
    sum = 0
    sum = int(s[0])
    for i in range(1, len(s)):
        sum += int(s[i])
        if abs(int(s[i]) - int(s[i - 1])) != 2:
               ok1 = 0
               break
    if sum % 10 == 0 and ok1:
        print("YES")
    else:
        print("NO")
    t -= 1