import math
t = int(input())

while t != 0:
    n = input()
    n1 = n[::-1]
    n = int(n)
    n1 =int(n1)
    
    if math.gcd(n, n1) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1