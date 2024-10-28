import math

t = int(input())

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        
    return n > 1


while t != 0:
    n = input()
    ok = 1
    cnt = 0
    for i in n:
        if nt(int(i)):
            cnt += 1
    if nt(len(n)) and cnt > len(n) - cnt:
        print("YES")
    else:
        print("NO")
    t -= 1