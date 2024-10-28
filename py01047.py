import math

t = int(input())


def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        
    return n > 1
while t != 0:
    s = input()

    #n = int(s[-4 : 0])
    n = s[-4:-1] + s[-1]
    n = int(n)
    if nt(n):
        print("YES")
    else:
        print("NO")
    #print(n)
    t -= 1