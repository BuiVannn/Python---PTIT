import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1
t = int(input())


while t != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)
    n = math.gcd(a, b)
    s = 0
    while n != 0:
        s += n % 10
        n //= 10

    #print(s)
    if nt(s):
        print("YES")
    else:
        print("NO")
    t -= 1