
import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    
    return n > 1


def check(n):
    cnt = 0
    for i in range(len(n)):
        if nt(int(n[i])):
            cnt += 1
    if nt(len(n)) and cnt > len(n) - cnt:
        return 1
    return 0

for _ in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")