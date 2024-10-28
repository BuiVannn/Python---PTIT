import math

t = int(input())

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    if n <= 1: return 0
    return 1
while t != 0:
    n = int(input())
    c = 0
    cnt = 0
    for i in range(1, n):
        c = math.gcd(n, i)
        if c == 1:
            cnt += 1
    #print(cnt)
    if nt(cnt) != 0:
        print("YES")
    else: print("NO")
    t -= 1